import ollama

client = ollama.Client(
    host="http://ollama:11434"
)


def summarize_news(text):

    prompt = f"""
    You are the journalist assistant for a news platform. 
    Your task is to read the given news article and provide a concise summary in the form of 3 bullet points. 
    Each bullet point should capture a key aspect of the article, such as the main event, important details, and any relevant context or implications.
    
    Article:
    {text}
    """

    response = client.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]