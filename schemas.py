from pydantic import BaseModel, Field


# -----------------------------
# INPUT MODEL (BALL EVENT)
# -----------------------------
class BallEvent(BaseModel):
    shot: str
    bat_runs: int = Field(ge=0, le=6)
    is_legal: bool = True


# -----------------------------
# HISTORY MODEL (FOR ANALYTICS ONLY)
# -----------------------------
class HistoricalShot(BaseModel):
    shot: str
    runs: int


# -----------------------------
# WAGON WHEEL ENTRY
# -----------------------------
class ShotEntry(BaseModel):
    shot: str
    runs: int
    angle: float


# -----------------------------
# STRONG ZONE OUTPUT
# -----------------------------
class Zone(BaseModel):
    name: str
    strength: int


# -----------------------------
# FINAL BATTER STATE (OUTPUT)
# -----------------------------
class BatterState(BaseModel):
    name: str
    runs: int = 0
    balls: int = 0
    fours: int = 0
    sixes: int = 0

    # computed fields (NEVER user input)
    strike_rate: float = 0.0
    wagon_wheel: list[ShotEntry] = []
    strong_zones: list[Zone] = []