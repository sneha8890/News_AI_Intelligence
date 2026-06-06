import streamlit as st
import requests

st.set_page_config(layout="wide")

article = st.session_state.get(
    "selected_news"
)

if not article:

    st.warning(
        "No article selected"
    )

    st.stop()

st.title(
    article.get("title")
)

if article.get("urlToImage"):

    st.image(
        article["urlToImage"],
        use_container_width=True
    )

source = (
    article
    .get("source", {})
    .get("name", "Unknown")
)

st.caption(
    f"Source: {source}"
)

st.divider()

description = article.get(
    "description",
    ""
)

if description:

    with st.spinner(
        "Generating AI summary..."
    ):

        try:

            response = requests.post(
                "http://localhost:8000/summarize",
                json={
                    "article": description
                }
            )

            summary = (
                response.json()
                .get("summary")
            )

            st.subheader(
                "🤖 AI Summary"
            )

            st.markdown(summary)

        except Exception:

            st.warning(
                "Summary unavailable"
            )

st.divider()

st.subheader("Article")

st.write(
    article.get(
        "content",
        article.get(
            "description",
            ""
        )
    )
)

st.link_button(
    "Read Original Article",
    article["url"]
)