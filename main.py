from fastapi import FastAPI, HTTPException, Security, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import os
from dotenv import load_dotenv
import json

load_dotenv()

app = FastAPI()
bearer_scheme = HTTPBearer()


@app.get("/")
async def root():
    return "goopi is running"


from services import gnews, goose


@app.get("/gnews")
def gnews_root(
    q: str = Query(None),
    token: HTTPAuthorizationCredentials = Security(bearer_scheme),
):

    if token or q is None:
        if token.scheme == "Bearer":
            api_key = token.credentials
            if api_key == os.getenv("API_KEY"):
                return gnews(q)

    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/goose")
async def goose_root(
    gnews_url: str = Query(None),
    token: HTTPAuthorizationCredentials = Security(bearer_scheme),
):

    if token or gnews_url is None:
        if token.scheme == "Bearer":
            api_key = token.credentials
            if api_key == os.getenv("API_KEY"):
                return goose(gnews_url)

    raise HTTPException(status_code=401, detail="Invalid credentials")
