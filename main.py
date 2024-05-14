from fastapi import FastAPI, HTTPException, Security, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.staticfiles import StaticFiles

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
bearer_scheme = HTTPBearer()

import os
import markdown
from fastapi.responses import HTMLResponse


def layout(title, html):
    return f"""
<!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <link rel="stylesheet" href="/static/markdown.module.css">

        </head>
        <body class="markdown-body">
        <header>
        <h1>{title}</h1>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/documentation">Documentation</a></li>
                    <li><a href="/changelog">Change Log</a></li>
                    <li><a href="/apikey">Api Key</a></li>
                </ul>
            </nav>
        </header>
            
        <main>
            {html}
        </main>

        <footer>
            <p>&copy; 2024 Goopi. All rights reserved. Powered by The Polygon</p>
        </footer>

        </body>
        </html>
"""


@app.get("/")
async def root():
    if not os.path.exists("README.md"):
        raise HTTPException(status_code=404, detail="File not found")

    with open("README.md", "r") as file:
        file_content = file.read()

    markdown_content = file_content

    html_content = markdown.markdown(markdown_content)

    return HTMLResponse(content=layout("Goopi API", html_content), status_code=200)


@app.get("/documentation")
def docs():
    if not os.path.exists("DOCS.md"):
        raise HTTPException(status_code=404, detail="File not found")

    with open("DOCS.md", "r") as file:
        file_content = file.read()

    markdown_content = file_content

    html_content = markdown.markdown(markdown_content)

    return HTMLResponse(
        content=layout("Goopi API - Documentation", html_content), status_code=200
    )


@app.get("/changelog")
async def changelog():
    if not os.path.exists("CHANGELOG.md"):
        raise HTTPException(status_code=404, detail="File not found")

    with open("CHANGELOG.md", "r") as file:
        file_content = file.read()

    markdown_content = file_content

    html_content = markdown.markdown(markdown_content)

    return HTMLResponse(
        content=layout("Goopi API - Change Log", html_content), status_code=200
    )


from services import gnews, goose


@app.get("/gnews")
def gnews_root(
    query: str = Query(min_length=1, max_length=255),
    lang: str = Query(
        default="ar",
        description="Language code (ar or en)",
        min_length=2,
        max_length=2,
        regex="^(ar|en)$",
    ),
    region: str = Query(
        default="IQ",
        description="Region code (US or IQ)",
        min_length=2,
        max_length=2,
        regex="^(IQ|US)$",
    ),
    period: str = Query(
        default="1d",
        description="[int]s, [int]h, [int]d, [int]w, [int]m, [int]y",
        min_length=3,
        max_length=3,
        regex="^\d+[swmhd]$",
    ),
    token: HTTPAuthorizationCredentials = Security(bearer_scheme),
):
    if token:
        if token.scheme == "Bearer":
            api_key = token.credentials
            if api_key == os.getenv("API_KEY"):
                return gnews(query=query, lang=lang, region=region, period=period)

    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/goose")
def goose_root(
    gnews_url: str,
    token: HTTPAuthorizationCredentials = Security(bearer_scheme),
):
    if gnews_url is None or "":
        raise HTTPException(status_code=400, detail="`gnews_url` url param is missing")
    elif token and gnews_url is not None or "":
        if token.scheme == "Bearer":
            api_key = token.credentials
            if api_key == os.getenv("API_KEY"):
                return goose(gnews_url)

    raise HTTPException(status_code=401, detail="Invalid credentials")
