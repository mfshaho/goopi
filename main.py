from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "goopi is running"
