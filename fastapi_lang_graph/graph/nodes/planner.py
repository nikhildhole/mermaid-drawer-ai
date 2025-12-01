from langchain.messages import SystemMessage
from fastapi_lang_graph.graph.models.gemini import gemini

prompt = """
You are a mermaid syntax validator.
"""


def planner(state: dict):
    """Mermaid syntax validator"""

    return {
        "messages": [
            gemini.invoke(
                [
                    SystemMessage(
                        content=prompt
                    )
                ]
                + state["messages"]
            )
        ],
        "llm_calls": state.get('llm_calls', 0) + 1
    }