
from fastapi_lang_graph.graph.agents.mermaid_validator import mermaid_validator_agent


def mermaid_validator(state: dict):
    """Mermaid syntax validator"""

    messages = {"messages": state["messages"]}
    result = mermaid_validator_agent.invoke(messages)

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }