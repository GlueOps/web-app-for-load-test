from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from io import BytesIO

app = FastAPI()

@app.get("/v1/qr")
def generate_qr(url: str):
    return "yolo"
