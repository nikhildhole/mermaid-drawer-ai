
from fastapi_lang_graph.graph.agents.requirements_gatherer import requirements_gatherer_agent


def requirements_gatherer(state: dict):
    """Requirements gatherer"""

    messages = {"messages": state["messages"]}
    result = requirements_gatherer_agent.invoke(messages)

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }