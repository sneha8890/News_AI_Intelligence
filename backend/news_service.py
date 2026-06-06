# ...existing code...
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Match the name used in your .env; change to "NEWS_API_KEY" if you rename the variable there
API_KEY = os.getenv("API_KEY")


def get_news(category):
    if not API_KEY:
        raise RuntimeError("API key not set. Add API_KEY to your .env or change this code to read NEWS_API_KEY.")

    category_mapping = {
        "Technology": "technology",
        "Finance": "business",
        "Sports": "sports",
        "Entertainment": "entertainment",
        "World News": "general"
    }

    api_category = category_mapping.get(category, "general")

    url = "https://newsapi.org/v2/top-headlines"
    params = {"category": api_category, "pageSize": 10, "apiKey": API_KEY}

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data.get("articles", [])
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch news for {category}: {e}")
        return []