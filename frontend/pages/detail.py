import requests
import streamlit as st

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
    article.get(
        "title",
        ""
    )
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

published = article.get(
    "publishedAt",
    ""
)[:10]

st.caption(
    f"{source} • {published}"
)

st.divider()

with st.spinner(
    "Generating AI Summary..."
):

    try:

        response = requests.post(
            "http://localhost:8000/summarize",
            json={
                "title": article.get(
                    "title",
                    ""
                ),
                "description": article.get(
                    "description",
                    ""
                ),
                "content": article.get(
                    "content",
                    ""
                ),
                "url": article.get(
                    "url",
                    ""
                )
            }
        )

        summary = (
            response.json()
            .get(
                "summary",
                ""
            )
        )

        st.subheader(
            "🤖 AI Summary"
        )

        st.markdown(
            summary
        )

    except Exception:

        st.warning(
            "Summary unavailable"
        )

st.divider()

st.link_button(
    "Read Original Article",
    article["url"]
)

