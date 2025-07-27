from fastapi import FastAPI, Request
from pydantic import BaseModel
from mcp_server import route_task

app = FastAPI()

class ProcessRequest(BaseModel):
    task: str
    text: str

@app.post("/process")
def process(request: ProcessRequest):
    result = route_task(request.task, request.text)
    return result 