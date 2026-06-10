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

titles = []
descriptions = []

for article in articles:

    title = article.get(
        "title",
        ""
    )

    description = article.get(
        "description",
        ""
    )

    if title:
        titles.append(title)

    if description:
        descriptions.append(description)

with st.spinner(
    "Generating AI Summary..."
):

    try:

        response = requests.post(
            "http://localhost:8000/analyse",
            json={
                "titles": titles,
                "descriptions": descriptions
            }
        )

        data = response.json()
        print(type(data))

        col1,col2= st.columns(2)

        with col1:
            st.subheader(
                "Trends"
            )

            for point in data.get(
                "trends",
                []
            ):
                st.markdown(
                    f"• {point}"
                )
        
        with col2:
            st.subheader(
                "Entities"
            )

            for point in data.get(
                "entities",
                []
            ):
                st.markdown(
                    f"• {point}"
                )

        st.subheader(
            "Most Important Updates"
        )

        for point in data.get(
            "updates",
            []
        ):
            st.markdown(
                f"• {point}"
            )
    except Exception as e:

        st.write(e)

