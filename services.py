import requests

from GoogleNews import GoogleNews
from bs4 import BeautifulSoup


def gnews(q):

    googlenews = GoogleNews(lang="ar", region="IQ")

    googlenews.set_lang("ar")
    googlenews.set_period("7d")
    googlenews.get_news(f"{str(q)}", True)

    result = googlenews.results(sort=True)

    return result


from goose3 import Goose


def goose(gnews_url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip",
            "Connection": "keep-alive",
        }
        cookies = {"CONSENT": "YES+cb.20220419-08-p0.cs+FX+111"}
        r = requests.get(
            (gnews_url if gnews_url.startswith("http") else f"https://{gnews_url}"),
            headers=headers,
            cookies=cookies,
        )
        soup = BeautifulSoup(r.text, "html.parser")
        url = soup.find_all("a", attrs={"jsname": "tljFtd"})[0].get("href")

        g = Goose()
        article = g.extract(url=url)
        return {
            "title": (article.title if article.title is not None else "NOT AVAILABLE"),
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
        print(f"Error processing {gnews_url}: {e}")
        return None
