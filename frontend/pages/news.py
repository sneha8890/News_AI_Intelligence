import streamlit as st
st.set_page_config(layout="wide")

st.title("News Articles")
st.write("Displaying articles for category: ", st.session_state.get("icon_category", "🌍"), st.session_state.get("selected_category", "World"))

import requests

selected_category = st.session_state["selected_category"]["title"]

response = requests.get(
    "http://127.0.0.1:8000/news",
    params={
        "category": selected_category
    }
)

data = response.json()

articles = data["articles"]

for article in articles:

    with st.container(border=True):

        st.subheader(article["title"])

        st.write(article.get("description", ""))

        if st.button(
            "Read More",
            key=article["title"]
        ):

            st.session_state["selected_news"] = {
                "title": article["title"],
                "summary": [
                    article.get("description", "")
                ],
                "url": article["url"]
            }

            st.switch_page("pages/detail.py")