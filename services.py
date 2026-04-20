from collections import defaultdict
from schemas import BatterState, BallEvent, HistoricalShot, ShotEntry, Zone


SHOT_MAP = {
    "cover_drive": 30,
    "straight_drive": 90,
    "on_drive": 120,
    "square_cut": 0,
    "pull_shot": 200,
    "hook_shot": 240,
    "sweep": 270,
    "lofted_drive": 80,
    "flick": 150
}


# 🧠 INTERNAL PAYLOAD WRAPPER (does NOT affect API)
class Payload:
    def __init__(self, state, event, history):
        self.state = state
        self.event = event
        self.history = history


def calculate_sr(runs: int, balls: int) -> float:
    if balls == 0:
        return 0.0
    return round((runs / balls) * 100, 2)


def get_zone(angle: float) -> str:
    if 0 <= angle < 60:
        return "off_side"
    elif 60 <= angle < 140:
        return "straight"
    elif 140 <= angle < 220:
        return "leg_side"
    else:
        return "fine_leg"


def compute_strong_zones(history: list[HistoricalShot]) -> list[Zone]:
    zone_count = defaultdict(int)

    for h in history:
        angle = SHOT_MAP.get(h.shot, 0)
        zone = get_zone(angle)

        if h.runs >= 4:
            zone_count[zone] += 1

    return [
        Zone(name=z, strength=c)
        for z, c in sorted(zone_count.items(), key=lambda x: -x[1])
    ]


# 🏏 MAIN ENGINE (now uses payload internally)
def update_batter(state: BatterState, event: BallEvent, history: list[HistoricalShot]):

    payload = Payload(state, event, history)

    s = payload.state
    e = payload.event
    h = payload.history

    # ------------------
    # Batting logic
    # ------------------
    s.runs += e.bat_runs

    if e.bat_runs == 4:
        s.fours += 1
    elif e.bat_runs == 6:
        s.sixes += 1

    if e.is_legal:
        s.balls += 1

    # ------------------
    # Wagon wheel
    # ------------------
    angle = SHOT_MAP.get(e.shot, 0)

    if e.bat_runs > 0:
        s.wagon_wheel.append(
            ShotEntry(
                shot=e.shot,
                runs=e.bat_runs,
                angle=angle
            )
        )

    # ------------------
    # Derived metrics
    # ------------------
    s.strike_rate = calculate_sr(s.runs, s.balls)

    s.strong_zones = compute_strong_zones(h)

    return s