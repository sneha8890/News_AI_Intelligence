from fastapi import FastAPI
from pydantic import BaseModel

from news_service import get_news
from ollama_service import summarize_news

app = FastAPI()


class SummaryRequest(BaseModel):
    article: str


@app.get("/news")
def news(category: str):

    return get_news(category)


@app.post("/summarize")
def summarize(request: SummaryRequest):

    summary = summarize_news(
        request.article
    )

    return {
        "summary": summary
    }