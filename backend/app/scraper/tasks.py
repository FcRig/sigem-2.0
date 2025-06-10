import requests
from requests.sessions import Session

session = Session()

def scrape_page(url: str):
    response = session.get(url)
    response.raise_for_status()
    return {"url": url, "content": response.text[:200]}
