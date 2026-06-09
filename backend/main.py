from fastapi import FastAPI
from pydantic import BaseModel

from news_service import get_news
from ollama_services import summarize_news
from ollama_services import analyse_news

app = FastAPI()

class AnalyseRequest(
    BaseModel
):
    titles: list[str]
    descriptions: list[str]

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
    print(type(summary))
    return summary


@app.post("/analyse")
def analyse(
    request: AnalyseRequest
):

    return analyse_news(
        request.titles,
        request.descriptions
    )