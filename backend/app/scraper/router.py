from fastapi import APIRouter, Depends
from .tasks import scrape_page

router = APIRouter()

@router.get('/')
def scrape(url: str):
    return scrape_page(url)
