import streamlit as st

st.set_page_config(layout="wide")

news = st.session_state.get("selected_news")

if not news:

    st.warning("No news selected")

    st.stop()

st.title(news["title"])

st.write("## Full Story")

st.write(
    '''
    This is where the complete article
    summary will come later using AI.
    '''
)

st.write("## Key Highlights")

for point in news["summary"]:
    st.write(f"• {point}")

st.link_button(
    "Read Original Article",
    news["url"]
)