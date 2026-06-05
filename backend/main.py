from fastapi import FastAPI
from news_service import get_news

app = FastAPI()

@app.get("/news")
def news(category: str):
    return get_news(category)