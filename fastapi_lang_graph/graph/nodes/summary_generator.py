
from fastapi_lang_graph.graph.agents.summary_generator import summary_generator_agent


def summary_generator(state: dict):
    """Summary generator"""

    messages = {"messages": state["messages"]}
    result = summary_generator_agent.invoke(messages)

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }