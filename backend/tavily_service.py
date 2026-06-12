import os

from tavily import TavilyClient

client = TavilyClient(
    api_key=os.getenv(
        "TAVILY_API_KEY"
    )
)


def search_web(
    query
):

    response = client.search(
        query=query,
        max_results=5
    )

    context = ""

    for result in response["results"]:

        context += f"""
        Title:
        {result['title']}

        Content:
        {result['content']}

        ----------------
        """

    return context