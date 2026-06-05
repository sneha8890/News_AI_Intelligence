import streamlit as st
from streamlit_card import card

st.set_page_config(
    page_title="Categories",
    layout="wide"
)

st.title("📰 Choose News Category")

st.write("Select a category to explore latest news")

categories = [
    {
        "title": "World News",
        "text": "Latest updates from around the globe.",
        "image": "🌍"
    },
    {
        "title": "Technology",
        "text": "AI, gadgets, and tech trends.",
        "image": "💻"
    },
    {
        "title": "Finance",
        "text": "Markets, economy, and business news.",
        "image": "💰"
    },
    {
        "title": "Sports",
        "text": "Scores, highlights, and sports news.",
        "image": "🏅"
    },
    {
        "title": "Entertainment",
        "text": "Movies, TV, and celebrity news.",
        "image": "🎬"
    }
]

col1 = st.columns(1)[0]

for category in categories:

    with col1:

        clicked = card(
            title=category["title"],
            text=category["text"],
            image=category["image"],
            styles={
                "card": {
                    "width": "100%",
                    "height": "150px",
                    "border-radius": "20px",
                    "box-shadow": "0 4px 20px rgba(0,0,0,0.2)",
                    "background-color": "#1e293b",
                    "padding": "10px",
                },
                "title": {
                    "font-size": "14px",
                    "font-weight": "bold",
                    "color": "#38bdf8",
                },
                "text": {
                    "font-size": "10px",
                    "color": "#cbd5e1",
                }
            }
        )

        if clicked:
            st.session_state["selected_category"] = category
            st.switch_page("pages/news.py")