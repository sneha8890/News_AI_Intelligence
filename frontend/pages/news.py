import streamlit as st
st.set_page_config(layout="wide")

st.title("News Articles")
st.write("Displaying articles for category: ", st.session_state.get("icon_category", "🌍"), st.session_state.get("selected_category", "World"))

news_data = [

    {
        "title": "OpenAI launches new AI model",
        "summary": [
            "Model improves reasoning",
            "Faster response generation",
            "Enterprise adoption rising"
        ],
        "url": "https://openai.com/blog/new-model"
    },

    {
        "title": "NVIDIA stock surges",
        "summary": [
            "AI demand increasing",
            "Revenue exceeds estimates",
            "Market optimism rises"
        ],
        "url": "https://www.nvidia.com/en-us/"
    },

    {
        "title": "IPL finals announced",
        "summary": [
            "Teams finalized",
            "Massive fan excitement",
            "Record ticket sales"
        ],
        "url": "https://www.iplt20.com/"
    }

]

for news in news_data:

    with st.container(border=True):

        st.subheader(news["title"])

        for point in news["summary"]:
            st.write(f"• {point}")

        if st.button(
            "Read More",
            key=news["title"]
        ):

            st.session_state["selected_news"] = news

            st.switch_page("pages/detail.py")