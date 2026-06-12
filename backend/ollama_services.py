import requests
import trafilatura
import ollama
import json

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

        if text and len(text) > 200:

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
            """

    prompt = f"""
        You are a senior news intelligence analyst.

        Analyze the following news article and return a structured intelligence report.

        Requirements:

        1. Summary
        - Generate exactly 5 bullet points.
        - Focus on the most important facts.
        - Include key people, organizations, companies, countries, technologies, or products when relevant.
        - Explain the significance and impact of the event.
        - Keep each bullet concise (maximum 2 sentences).

        2. Sentiment
        - Determine the overall sentiment of the article.
        - Allowed values:
            - Positive
            - Neutral
            - Negative

        3. Importance
        - Assign an importance score from 1 to 10.
        - Use the following guidance:
            - 1-3: Minor/local significance
            - 4-6: Moderate relevance
            - 7-8: Major national or industry impact
            - 9-10: Major global impact or highly significant event

        4. Entities
        - Extract exactly 5 important entities.
        - Prioritize:
            - People
            - Companies
            - Organizations
            - Countries
            - Technologies
            - Major events
        - Avoid generic words such as:
            "news", "report", "update", "article", "development"

        Output Rules:
        - Return ONLY valid JSON.
        - Do NOT include markdown.
        - Do NOT include explanations.
        - Do NOT wrap the response in ```json blocks.
        - Do NOT output any text before or after the JSON.
        - Ensure the JSON is directly parseable.

        Expected JSON format:

        {{
            "summary": [
                "bullet point 1",
                "bullet point 2",
                "bullet point 3",
                "bullet point 4",
                "bullet point 5"
            ],
            "sentiment": "Positive",
            "importance": 8,
            "entities": [
                "Entity 1",
                "Entity 2",
                "Entity 3",
                "Entity 4",
                "Entity 5"
            ]
        }}

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

    content = response["message"]["content"]
    return json.loads(content)

def analyse_news(
    titles,
    descriptions
):

    news_text = ""

    for idx in range(
        min(
            len(titles),
            len(descriptions)
        )
    ):

        news_text += f"""
        Article {idx + 1}

        Title:
        {titles[idx]}

        Description:
        {descriptions[idx]}

        --------------------
        """

    prompt = f"""
    You are a senior news intelligence analyst.

    Analyze all the news articles below and identify:

    1. Trends
       - Extract exactly 5 trending topics.
       - Topics should represent recurring themes.
       - Keep each topic short.

    2. Entities
       - Extract exactly 5 most important entities.
       - Prioritize people, companies, organizations,
         countries, technologies and events.

    3. Most Important Updates
       - Identify exactly 3 most important updates.
       - Each update should be one concise sentence.
       - Focus on developments that matter most today.

    Return ONLY valid JSON.

    Expected format:

    {{
        "trends": [
            "Trend 1",
            "Trend 2",
            "Trend 3",
            "Trend 4",
            "Trend 5"
        ],
        "entities": [
            "Entity 1",
            "Entity 2",
            "Entity 3",
            "Entity 4",
            "Entity 5"
        ],
        "updates": [
            "Update 1",
            "Update 2",
            "Update 3"
        ]
    }}

    News Articles:

    {news_text}
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

    content = response[
        "message"
    ][
        "content"
    ]

    try:

        return json.loads(
            content
        )

    except Exception as e:

        print(
            "Analyse Parse Error:",
            e
        )

        print(content)

        return {
            "trends": [],
            "entities": [],
            "updates": []
        }
    

def ask_news_ai(
    question,
    articles,
    messages
):

    news_context = ""

    conversation_context = ""

    for message in messages[-10:]:

        conversation_context += f"""
        {message["role"].upper()}:
        {message["content"]}
        """

    for article in articles:

        news_context += f"""
        Title:
        {article.get("title", "")}

        Description:
        {article.get("description", "")}

        Source:
        {article.get("source", {}).get("name", "")}

        ---------------------
        """

    prompt = f"""
You are a News Intelligence Assistant.

    Use ONLY the news articles below.

    Conversation History:

    {conversation_context}

    Current Question:

    {question}

    News Articles:

    {news_context}

    Rules:

    1. Use conversation history when needed.
    2. Use ONLY provided news.
    3. Do not use external knowledge.
    4. If answer not available return ONLY:

    NOT_FOUND

    5. Keep answers concise.
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

    return (
        response["message"]["content"]
    )