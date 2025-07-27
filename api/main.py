from fastapi import FastAPI, Request
from pydantic import BaseModel
from mcp_server import route_task
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

@app.get("/")
def root():
    return FileResponse(os.path.join(os.path.dirname(__file__), "static", "index.html"))

class ProcessRequest(BaseModel):
    task: str
    text: str

@app.post("/process")
def process(request: ProcessRequest):
    result = route_task(request.task, request.text)
    return result 