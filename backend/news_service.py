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

    if category == "World News":

        response = requests.get(
            "https://newsapi.org/v2/everything",
            params={
                "q": "world",
                "language": "en",
                "sortBy": "publishedAt",
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
                "country": "us",
                "pageSize": 100,
                "apiKey": API_KEY
            }
        )

    data = response.json()

    articles = data.get(
        "articles",
        []
    )

    unique_articles = []

    seen_titles = set()

    seen_sources = set()

    for article in articles:

        title = article.get(
            "title",
            ""
        )

        source = (
            article
            .get("source", {})
            .get("name", "")
        )

        if not title:
            continue

        normalized_title = (
            title
            .lower()
            .strip()
        )

        if normalized_title in seen_titles:
            continue

        # Prefer different sources
        if source in seen_sources and len(unique_articles) >= 10:
            continue

        seen_titles.add(
            normalized_title
        )

        seen_sources.add(
            source
        )

        unique_articles.append(
            article
        )

        if len(unique_articles) == 10:
            break

    data["articles"] = unique_articles

    return data