import streamlit as st

st.set_page_config(layout="wide")

st.title("📰 Choose Category")

categories = [
    {
        "title":"World News",
        "icon":"🌍",
        "desc":"Latest global news"
    },
    {
        "title":"Technology",
        "icon":"💻",
        "desc":"AI, Gadgets and Startups"
    },
    {
        "title":"Finance",
        "icon":"💰",
        "desc":"Markets and Economy"
    },
    {
        "title":"Sports",
        "icon":"🏏",
        "desc":"Cricket and Sports"
    },
    {
        "title":"Entertainment",
        "icon":"🎬",
        "desc":"Movies and Celebrities"
    }
]

col1,col2 = st.columns(2)

for idx,category in enumerate(categories):

    current_col = col1 if idx % 2 == 0 else col2

    with current_col:

        with st.container(border=True):

            st.markdown(
                f"""
                ## {category['icon']} {category['title']}

                {category['desc']}
                """
            )

            if st.button(
                f"Open {category['title']}",
                key=category["title"],
                use_container_width=True
            ):

                st.session_state["selected_category"] = category

                st.switch_page("pages/news.py")