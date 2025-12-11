
from fastapi_lang_graph.graph.agents.mermaid_generator import mermaid_generator_agent


def mermaid_generator(state: dict):
    """Mermaid syntax generator"""

    messages = {"messages": state["messages"]}
    result = mermaid_generator_agent.invoke(messages)

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }