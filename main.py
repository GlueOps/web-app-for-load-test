from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
import shutil
import time

app = FastAPI()

@app.get("/uploadfile", response_class=HTMLResponse)
async def get():
    html_content = """
    <html>
        <head>
            <title>Upload a File</title>
        </head>
        <body>
            <h1>Upload a File</h1>
            <form action="/v1/uploadfile/" enctype="multipart/form-data" method="post">
                <input type="file" name="file"><br><br>
                <input type="submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/v1/sleep")
def delay_response(ms: int):
    if ms < 0 or ms > 60000:  # Limit sleep time to a maximum of 11 seconds
        raise HTTPException(status_code=400, detail="Invalid ms value. Must be between 0 and 60000.")
    
    time.sleep(ms / 1000)
    return JSONResponse(content={"status": "success", "time_slept_ms": ms }, status_code=200)

@app.post("/v1/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    start_time = time.time()
    file_location = f"{file.filename}"
    with open(file_location, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # time in milliseconds
        
    return {
        "info": "success",
        "filename": file.filename,
        "time_taken_ms": elapsed_time
    }
