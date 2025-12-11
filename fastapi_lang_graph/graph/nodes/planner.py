
from fastapi_lang_graph.graph.agents.planner import planner_agent


def planner(state: dict):
    """Mermaid syntax generator"""

    messages = {"messages": state["messages"]}
    result = planner_agent.invoke(messages)

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }