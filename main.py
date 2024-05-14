from fastapi import FastAPI

app = FastAPI(__name__)


@app.get("/")
def root():
    return "goopi is running"
