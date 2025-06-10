from fastapi import FastAPI
from .auth import router as auth_router
from .scraper import router as scraper_router

app = FastAPI(title="Sigem Scraper API")

app.include_router(auth_router, prefix="/auth")
app.include_router(scraper_router, prefix="/scraper")

@app.get("/")
def read_root():
    return {"message": "Sigem 2.0 backend"}
