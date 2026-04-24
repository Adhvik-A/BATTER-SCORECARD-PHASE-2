from fastapi import FastAPI, HTTPException
from schemas import BatterScorecardRequest
from services import build_scorecard

app = FastAPI(
    title="Batter Scorecard API",
    description="Build full batter scorecard from ball-by-ball data",
    version="1.0"
)



@app.get("/", tags=["Root"], summary="API Root", description="Basic API info endpoint")
def root():
    return {
        "meta": {
            "api": "batter-scorecard",
            "version": "1.0",
            "status": "running"
        },
        "data": {
            "message": "Batter Scorecard API is live",
            "endpoints": [
                "/health",
                "/batter-scorecard"
            ]
        },
        "errors": None
    }


@app.get("/health", tags=["Health"], summary="Health Check")
def health():
    return {"status": "ok"}



@app.post(
    "/batter-scorecard",
    tags=["Scorecard"],
    summary="Generate Batter Scorecard",
    description="Processes full ball-by-ball input and returns complete batter scorecard"
)
def batter_scorecard(payload: BatterScorecardRequest):

    try:
        result = build_scorecard(payload)

        return {
            "meta": {
                "api": "batter-scorecard",
                "version": "1.0",
                "status": "success"
            },
            "data": result,
            "errors": None
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
