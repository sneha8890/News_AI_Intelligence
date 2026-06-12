from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from news_service import get_news
from ollama_services import (
    summarize_news,
    analyse_news,
    ask_news_ai
)

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

class AskRequest(BaseModel):

    question: str

    articles: list

    messages: Optional[list] = []


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

@app.post("/ask")
def ask(
    request: AskRequest
):

    answer = ask_news_ai(
        request.question,
        request.articles,
        request.messages
    )

    return {
        "answer": answer
    }