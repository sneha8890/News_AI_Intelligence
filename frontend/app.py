import streamlit as st

st.set_page_config(
    page_title="News Intelligence",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    font-size:20px;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="main-title">🧠 News Intelligence</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">AI Powered News Analysis Platform</p>',
    unsafe_allow_html=True
)

st.divider()

c1,c2,c3 = st.columns([1,1,1])

with c2:
    if st.button("Continue", use_container_width=True):
        st.switch_page("pages/categories.py")