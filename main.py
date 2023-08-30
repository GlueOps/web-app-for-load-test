from fastapi import FastAPI, File, UploadFile, HTTPException, Response
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import time

app = FastAPI()

@app.get("/v1/sleep")
def delay_response(ms: int):
    if ms < 0 or ms > 11000:  # Limit sleep time to a maximum of 11 seconds
        raise HTTPException(status_code=400, detail="Invalid ms value. Must be between 0 and 11000.")
    
    time.sleep(ms / 1000)
    return JSONResponse(content={"status": "success", "time_slept_ms": ms }, status_code=200)

@app.post("/v1/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"uploaded_files/{file.filename}"
    with open(file_location, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {
        "info": "success",
        "filename": file.filename
    }
