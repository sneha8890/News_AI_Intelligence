import streamlit as st

st.set_page_config(
    page_title="News Intelligence App",
    page_icon="🧠",
    layout="wide"
)


# CUSTOM CSS


st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }

    .title {
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        color: white;
        margin-top: 120px;
    }

    .subtitle {
        text-align: center;
        font-size: 22px;
        color: #cbd5e1;
        margin-bottom: 50px;
    }

    .stButton > button {
        width: 220px;
        height: 60px;
        font-size: 22px;
        border-radius: 15px;
        background-color: #2563eb;
        color: white;
        border: none;
    }

    .btn-center {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="title">🧠 NEWS INTELLIGENCE APP</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered real-time news platform</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,1,1])

with col2:
    if st.button("Continue"):
        st.switch_page("pages/categories.py")