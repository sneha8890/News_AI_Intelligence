import requests
import streamlit as st

st.set_page_config(layout="wide")

selected_category = st.session_state.get(
    "selected_category"
)

if not selected_category:

    st.warning(
        "Please select category"
    )

    st.stop()

st.title(
    f"{selected_category['icon']} {selected_category['title']}"
)

try:

    response = requests.get(
        "http://localhost:8000/news",
        params={
            "category": selected_category["title"]
        }
    )

    data = response.json()

    articles = data.get(
        "articles",
        []
    )

except Exception as e:

    st.error(
        f"Backend Error: {e}"
    )

    st.stop()

st.subheader(
    f"{len(articles)} Latest Articles"
)

for article in articles:

    with st.container(border=True):

        if article.get("urlToImage"):

            st.image(
                article["urlToImage"],
                use_container_width=True
            )

        st.subheader(
            article.get(
                "title",
                "No Title"
            )
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

        st.write(
            article.get(
                "description",
                ""
            )
        )

        if st.button(
            "Read More",
            key=article["url"]
        ):

            st.session_state[
                "selected_news"
            ] = article

            st.switch_page(
                "pages/detail.py"
            )