from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import BatterState, BallEvent, HistoricalShot
from services import update_batter

app = FastAPI(title="Cricket Batter Analytics API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/ball", response_model=BatterState)
def ball_event(
    state: BatterState,
    event: BallEvent,
    history: list[HistoricalShot] = []
):
    return update_batter(state, event, history)