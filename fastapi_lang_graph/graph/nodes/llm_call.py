from langchain.messages import SystemMessage
from fastapi_lang_graph.graph.models.gemini import gemini

def llm_call(state: dict):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [
            gemini.invoke(
                [
                    SystemMessage(
                        content="You are a helpful assistant."
                    )
                ]
                + state["messages"]
            )
        ],
        "llm_calls": state.get('llm_calls', 0) + 1
    }