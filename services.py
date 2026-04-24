from fastapi import HTTPException
from schemas import BatterScorecardRequest, BatterScorecard


def calculate_sr(runs: int, balls: int) -> float:
    if balls == 0:
        return 0.0
    return round((runs / balls) * 100, 2)


def build_scorecard(payload: BatterScorecardRequest) -> BatterScorecard:

    runs = 0
    balls = 0
    fours = 0
    sixes = 0

    for event in payload.balls:

        if event.bat_runs < 0:
            raise HTTPException(status_code=400, detail="Invalid runs")

        runs += event.bat_runs

        if event.bat_runs == 4:
            fours += 1
        elif event.bat_runs == 6:
            sixes += 1

        if event.is_legal:
            balls += 1

    return BatterScorecard(
        player_id=payload.player_id,
        match_id=payload.match_id,
        innings_id=payload.innings_id,
        name=payload.name,
        runs=runs,
        balls=balls,
        fours=fours,
        sixes=sixes,
        strike_rate=calculate_sr(runs, balls)
    )
