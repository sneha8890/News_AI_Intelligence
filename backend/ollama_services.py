import requests
import trafilatura
import ollama


def get_article_text(url):

    try:

        headers = {
            "User-Agent":
            "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        downloaded = response.text

        text = trafilatura.extract(
            downloaded
        )

        if text and len(text) > 500:

            return text

    except Exception as e:

        print(
            "Scraping Failed:",
            e
        )

    return None


def summarize_news(article):

    article_text = None

    url = article.get(
        "url",
        ""
    )

    if url:

        article_text = get_article_text(
            url
        )

    if not article_text:

        article_text = f"""
            Title:
            {article.get('title', '')}

            Description:
            {article.get('description', '')}

            Content:
            {article.get('content', '')}
            """

    prompt = f"""
        You are an expert journalist assistant.

        Analyze the article and provide:

        - Exactly 5 bullet points
        - Mention key people, companies and organizations
        - Highlight important developments
        - Explain the impact
        - Mention future implications if available

        Article:

        {article_text}
    """

    response = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]