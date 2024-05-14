from fastapi import FastAPI, HTTPException, Security, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()

import os
from dotenv import load_dotenv

load_dotenv()

import requests

from GoogleNews import GoogleNews
from bs4 import BeautifulSoup


@app.get("/gnews")
def newsapi(
    q: str = Query(None),
    token: HTTPAuthorizationCredentials = Security(bearer_scheme),
):

    if token or q is None:
        if token.scheme == "Bearer":
            api_key = token.credentials
            if api_key == os.getenv("API_KEY"):
                googlenews = GoogleNews(lang="ar", region="IQ")

                googlenews.set_lang("ar")
                googlenews.set_period("7d")
                googlenews.get_news(f"{str(q)}", True)

                result = googlenews.results(sort=True)

                return result

    raise HTTPException(status_code=401, detail="Invalid credentials")


from goose3 import Goose


@app.get("/extractor")
def goopi(
    initial_url: str = Query(None),
    token: HTTPAuthorizationCredentials = Security(bearer_scheme),
):
    if token or initial_url is None:
        if token.scheme == "Bearer":
            api_key = token.credentials
            if api_key == os.getenv("API_KEY"):

                try:

                    headers = {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                        "Accept-Encoding": "gzip",
                        "Connection": "keep-alive",
                    }
                    cookies = {"CONSENT": "YES+cb.20220419-08-p0.cs+FX+111"}
                    r = requests.get(
                        (
                            initial_url
                            if initial_url.startswith("http")
                            else f"https://{initial_url}"
                        ),
                        headers=headers,
                        cookies=cookies,
                    )
                    soup = BeautifulSoup(r.text, "html.parser")
                    url = soup.find_all("a", attrs={"jsname": "tljFtd"})[0].get("href")

                    g = Goose()
                    article = g.extract(url=url)
                    return {
                        "title": (
                            article.title
                            if article.title is not None
                            else "NOT AVAILABLE"
                        ),
                        "description": (
                            article.opengraph.get("description")
                            if article.opengraph is not None
                            else "NOT AVAILABLE"
                        ),
                        "content": article.cleaned_text.split("\n"),
                        "image": (
                            article.opengraph.get("image")[0]
                            if article.opengraph.get("image") is not None
                            else "NOT AVAILABLE"
                        ),
                        "favicon": (
                            f"{article.meta_favicon}"
                            if article.meta_favicon.startswith("http")
                            else f"https://{article.domain}{article.meta_favicon}"
                        ),
                        "domain": article.domain,
                        "url": article.final_url,
                        "date": article.publish_date,
                    }
                except Exception as e:
                    print(f"Error processing {initial_url}: {e}")
                    return None


@app.post("/")
async def root(
    token: HTTPAuthorizationCredentials = Security(bearer_scheme),
):

    if token:
        if token.scheme == "Bearer":
            api_key = token.credentials
            if api_key == os.getenv("API_KEY"):
                return {"message": "AUTH YES"}

    raise HTTPException(status_code=401, detail="Invalid credentials")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
