from fastapi import FastAPI
from pydantic import BaseModel

from news_service import get_news
from ollama_services import summarize_news

app = FastAPI()


class SummaryRequest(BaseModel):
    title: str = ""
    description: str = ""
    content: str = ""
    url: str = ""


@app.get("/news")
def news(category: str):

    return get_news(category)


@app.post("/summarize")
def summarize(request: SummaryRequest):

    summary = summarize_news(
        {
            "title": request.title,
            "description": request.description,
            "content": request.content,
            "url": request.url
        }
    )

    return {
        "summary": summary
    }