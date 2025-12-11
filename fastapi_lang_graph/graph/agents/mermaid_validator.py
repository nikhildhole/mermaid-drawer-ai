from langchain.agents import create_agent
from langchain.tools import tool

from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite
from fastapi_lang_graph.services.redis import get_code
from fastapi_lang_graph.core.logging import logger

@tool
def get_current_code() -> str:
    """Get the current mermaid code."""
    logger.info("#############################")
    logger.info("get current code function called")
    logger.info("#############################")

    current_code = get_code()

    logger.info(f"Current mermaid code:\n{current_code}")

    return current_code


PROMPT = """
You are a mermaid code validator. Use the tools to get the current mermaid code and validate it. If there are any errors, describe them clearly.
"""

mermaid_validator_agent = create_agent(
    model=gemini_2_5_flash_lite,
    system_prompt=PROMPT,
    tools=[get_current_code]
)