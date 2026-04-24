from pydantic import BaseModel, Field
from enum import Enum


class Phase(str, Enum):
    powerplay = "powerplay"
    middle = "middle"
    death = "death"


class ExtraType(str, Enum):
    wide = "wide"
    no_ball = "no_ball"
    bye = "bye"
    leg_bye = "leg_bye"


class BallEvent(BaseModel):
    shot: str
    bat_runs: int = Field(ge=0, le=6)
    is_legal: bool = True
    phase: Phase | None = None
    extra_type: ExtraType | None = None


class BatterScorecardRequest(BaseModel):
    player_id: int
    match_id: int
    innings_id: int
    name: str
    balls: list[BallEvent]


class BatterScorecard(BaseModel):
    player_id: int
    match_id: int
    innings_id: int
    name: str
    runs: int
    balls: int
    fours: int
    sixes: int
    strike_rate: float
