import requests
import streamlit as st

st.set_page_config(
    layout="wide"
)

selected_category = (
    st.session_state.get(
        "selected_category"
    )
)

if not selected_category:

    st.warning(
        "Please select category"
    )

    st.stop()

if "messages" not in st.session_state:

    st.session_state["messages"] = []

st.title(
    f"🤖 Ask AI - {selected_category['title']}"
)

if st.button(
    "Clear Chat"
):

    st.session_state["messages"] = []

    st.rerun()

try:

    response = requests.get(
        "http://localhost:8000/news",
        params={
            "category":
            selected_category["title"]
        }
    )

    articles = (
        response.json()
        .get(
            "articles",
            []
        )
    )

except Exception as e:

    st.error(
        f"Backend Error: {e}"
    )

    st.stop()

# Show old messages every rerun
for message in st.session_state["messages"]:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )

question = st.chat_input(
    "Ask about today's news..."
)

if question:

    # Show user message immediately
    with st.chat_message(
        "user"
    ):
        st.write(
            question
        )

    # Save user message
    st.session_state["messages"].append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.spinner(
        "Thinking..."
    ):

        try:

            response = requests.post(
                "http://localhost:8000/ask",
                json={
                    "question": question,
                    "articles": articles,
                    "messages": st.session_state[
                        "messages"
                    ]
                }
            )

            if response.status_code != 200:

                st.error(
                    f"Backend Error: {response.text}"
                )

                st.stop()

            answer = (
                response.json()
                .get(
                    "answer",
                    ""
                )
            )

        except Exception as e:

            st.error(
                f"Request Failed: {e}"
            )

            st.stop()

    with st.chat_message(
        "assistant"
    ):

        st.write(
            answer
        )

    # Save assistant reply
    st.session_state["messages"].append(
        {
            "role": "assistant",
            "content": answer
        }
    )