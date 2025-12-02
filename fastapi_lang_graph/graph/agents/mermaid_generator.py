from langchain.agents import create_agent
from langchain.tools import tool

from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite
from fastapi_lang_graph.services.redis import get_current_code, write_code

@tool
def get_current_code() -> str:
    """Get the current mermaid code."""
    return get_current_code()

@tool
def write_to_current_code(new_code: str) -> bool:
    """Write to the current mermaid code."""
    return write_code(new_code)

PROMPT = """
You are a mermaid code generator. Use the tools to get the current mermaid code and update it as needed. At the end return summary of changes made.
"""

mermaid_generator_agent = create_agent(
    model=gemini_2_5_flash_lite,
    system_prompt=PROMPT,
    tools=[get_current_code, write_to_current_code]
)