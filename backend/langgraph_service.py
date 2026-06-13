from typing import TypedDict
from ollama_services import (
    ask_news_ai,
    ask_tavily
)

class AgentState(
    TypedDict
):

    question: str

    articles: list

    messages: list

    answer: str

def news_node(
    state
):

    answer = ask_news_ai(
        state["question"],
        state["articles"],
        state["messages"]
    )

    return {
        "answer": answer
    }

def route_decision(
    state
):

    if (
        state["answer"]
        .strip()
        == "NOT_FOUND"
    ):

        return "tavily"

    return "end"

def tavily_node(
    state
):

    answer = ask_tavily(
        state["question"]
    )

    return {
        "answer": answer
    }

from langgraph.graph import (
    StateGraph,
    END
)

graph_builder = StateGraph(
    AgentState
)

graph_builder.add_node(
    "news",
    news_node
)

graph_builder.add_node(
    "tavily",
    tavily_node
)

graph_builder.set_entry_point(
    "news"
)

graph_builder.add_conditional_edges(
    "news",
    route_decision,
    {
        "tavily": "tavily",
        "end": END
    }
)

graph_builder.add_edge(
    "tavily",
    END
)

graph = (
    graph_builder.compile()
)

def run_agent(
    question,
    articles,
    messages
):

    result = graph.invoke(
        {
            "question": question,
            "articles": articles,
            "messages": messages,
            "answer": ""
        }
    )

    return result["answer"]