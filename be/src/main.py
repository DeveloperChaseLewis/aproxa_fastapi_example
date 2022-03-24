import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root(request: Request):
    return { "message": "Hello World", "headers": request.headers }