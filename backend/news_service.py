import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def get_news(category):

    category_mapping = {
        "Technology": "technology",
        "Finance": "business",
        "Sports": "sports",
        "Entertainment": "entertainment"
    }

    if category == "Top Headlines":

        sources = (
            "bbc-news",
            "reuters",
            "associated-press"
        )

        response = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params={
                "sources": sources,
                "pageSize": 100,
                "apiKey": API_KEY
            }
        )

    else:

        response = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params={
                "category": category_mapping.get(
                    category,
                    "general"
                ),
                "pageSize": 100,
                "apiKey": API_KEY
            }
        )

    data = response.json()
    print(data)
    articles = data.get(
        "articles",
        []
    )


    unique_articles = []

    seen_titles = set()

    for article in articles:

        title = article.get(
            "title",
            ""
        )

        if not title:
            continue

        normalized_title = " ".join(
            title.lower().split()[:8]
        )

        if normalized_title in seen_titles:
            continue


        seen_titles.add(
            normalized_title
        )

        unique_articles.append(
            article
        )

        if len(unique_articles) == 10:
            break

    data["articles"] = unique_articles

    return data