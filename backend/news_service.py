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
        "Entertainment": "entertainment",
        "World News": "general"
    }

    api_category = category_mapping.get(category, "general")

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"category={api_category}"
        f"&language=en"
        f"&pageSize=5"
        f"&apiKey={API_KEY}"
    )

    response = requests.get(url)

    return response.json()