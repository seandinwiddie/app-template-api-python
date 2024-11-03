from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from typing import Dict, Any

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load initial state
def load_initial_state() -> Dict[str, Any]:
    try:
        with open("src/data/initialState.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception("Failed to read initialState.json")
    except json.JSONDecodeError:
        raise Exception("Failed to parse JSON")

initial_state = load_initial_state()

@app.get("/")
async def home():
    return {"message": "Welcome to the API"}

@app.get("/status")
async def status():
    return {"status": "OK"}

@app.get("/data")
async def get_data():
    return initial_state

@app.get("/{key}")
async def get_by_key(key: str):
    if key in initial_state:
        return {key: initial_state[key]}
    raise HTTPException(status_code=404, detail="Key not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
