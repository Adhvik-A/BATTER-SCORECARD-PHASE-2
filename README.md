# Batter Scorecard API

---

## API Objective

Build a full batter scorecard from ball-by-ball input.

---

## Endpoint

GET /
GET /health
POST /batter-scorecard

---

## Input Schema

```json
{
  "player_id": "int",
  "match_id": "int",
  "innings_id": "int",
  "name": "string",
  "balls": [
    {
      "shot": "string",
      "bat_runs": "int (0-6)",
      "is_legal": "boolean",
      "phase": "powerplay | middle | death (optional)",
      "extra_type": "wide | no_ball | bye | leg_bye (optional)"
    }
  ]
}
Output Schema
{
  "meta": {
    "api": "batter-scorecard",
    "version": "1.0",
    "status": "success"
  },
  "data": {
    "player_id": "int",
    "match_id": "int",
    "innings_id": "int",
    "name": "string",
    "runs": "int",
    "balls": "int",
    "fours": "int",
    "sixes": "int",
    "strike_rate": "float"
  },
  "errors": null
}
Example Request
{
  "player_id": 18,
  "match_id": 101,
  "innings_id": 1,
  "name": "Virat Kohli",
  "balls": [
    { "shot": "cover_drive", "bat_runs": 4, "is_legal": true },
    { "shot": "pull_shot", "bat_runs": 6, "is_legal": true },
    { "shot": "defence", "bat_runs": 0, "is_legal": true }
  ]
}
Example Response
{
  "meta": {
    "api": "batter-scorecard",
    "version": "1.0",
    "status": "success"
  },
  "data": {
    "player_id": 18,
    "match_id": 101,
    "innings_id": 1,
    "name": "Virat Kohli",
    "runs": 10,
    "balls": 3,
    "fours": 1,
    "sixes": 1,
    "strike_rate": 333.33
  },
  "errors": null
}
Example Request (GET /)
curl http://localhost:8000/
Example Response (GET /)
{
  "meta": {
    "api": "batter-scorecard",
    "version": "1.0",
    "status": "running"
  },
  "data": {
    "message": "API is live",
    "endpoints": [
      "/",
      "/health",
      "/batter-scorecard"
    ]
  },
  "errors": null
}
Example Request (GET /health)
curl http://localhost:8000/health
Example Response (GET /health)
{
  "status": "ok"
}
Validation Errors
400 Bad Request — Invalid Runs
{
  "detail": "Invalid runs"
}
400 Bad Request — Invalid Shot Type
{
  "detail": "Invalid shot type"
}
422 Unprocessable Entity — Missing Fields
{
  "detail": "Field required"
}
422 Unprocessable Entity — Invalid Data Type
{
  "detail": "value is not a valid integer"
}
Integration Usage
cURL
curl -X POST "http://localhost:8000/batter-scorecard" \
-H "Content-Type: application/json" \
-d '{
  "player_id": 18,
  "match_id": 101,
  "innings_id": 1,
  "name": "Virat Kohli",
  "balls": [
    { "shot": "cover_drive", "bat_runs": 4, "is_legal": true }
  ]
}'
Python (requests)
import requests

url = "http://localhost:8000/batter-scorecard"

payload = {
    "player_id": 18,
    "match_id": 101,
    "innings_id": 1,
    "name": "Virat Kohli",
    "balls": [
        {"shot": "cover_drive", "bat_runs": 4, "is_legal": True}
    ]
}

response = requests.post(url, json=payload)
print(response.json())
JavaScript (fetch)
fetch("http://localhost:8000/batter-scorecard", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    player_id: 18,
    match_id: 101,
    innings_id: 1,
    name: "Virat Kohli",
    balls: [
      { shot: "cover_drive", bat_runs: 4, is_legal: true }
    ]
  })
})
.then(res => res.json())
.then(data => console.log(data));
