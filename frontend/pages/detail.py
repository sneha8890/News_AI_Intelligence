import requests
import streamlit as st
import json
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

        data = response.json()
        print(type(data))

        st.subheader(
            "🤖 AI Summary"
        )

        for point in data.get(
            "summary",
            []
        ):
            st.markdown(
                f"• {point}"
            )

        st.subheader(
            "😊 AI Sentiment"
        )

        sentiment = data.get(
            "sentiment",
            "Unknown"
        )

        if sentiment == "Positive":
            st.success(sentiment)

        elif sentiment == "Negative":
            st.error(sentiment)

        else:
            st.info(sentiment)

        st.subheader(
            "⭐ Importance"
        )

        importance = data.get(
            "importance",
            "N/A"
        )

        st.metric(
            "Importance Score",
            f"{importance}/10"
        )

        st.subheader(
            "🏷️ Entities Recognized"
        )

        entities = data.get(
            "entities",
            []
        )

        if entities:

            cols = st.columns(
                min(
                    len(entities),
                    5
                )
            )

            for idx, entity in enumerate(entities):

                cols[idx].chip = entity

                cols[idx].markdown(
                    f"`{entity}`"
                )

        else:

            st.write(
                "No entities found"
            )
    except Exception as e:

        st.write(e)

st.divider()

st.link_button(
    "Read Original Article",
    article["url"]
)

