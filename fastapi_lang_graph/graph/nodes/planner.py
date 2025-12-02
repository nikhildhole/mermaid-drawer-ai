from langchain.messages import SystemMessage
from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite

prompt = """
You are a mermaid syntax validator.
"""


def planner(state: dict):
    """Mermaid syntax validator"""

    return {
        "messages": [
            gemini_2_5_flash_lite.invoke(
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