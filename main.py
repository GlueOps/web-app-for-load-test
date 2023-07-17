from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
import time

app = FastAPI()

@app.get("/v1/sleep")
def delay_response(ms: int):
    if ms < 0 or ms > 11000:  # Limit sleep time to a maximum of 11 seconds
        raise HTTPException(status_code=400, detail="Invalid ms value. Must be between 0 and 11000.")
    
    time.sleep(ms / 1000)
    return JSONResponse(content={"status": "success", "time_slept_ms": ms }, status_code=200)
