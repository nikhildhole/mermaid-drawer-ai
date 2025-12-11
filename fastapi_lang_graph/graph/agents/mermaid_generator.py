from langchain.agents import create_agent
from langchain.tools import tool

from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite
from fastapi_lang_graph.services.redis import get_code, write_code
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

@tool
def write_to_current_code(new_code: str) -> bool:
    """Write to the current mermaid code."""
    logger.info("#############################")
    logger.info("write to current code function called")
    logger.info("#############################")

    logger.info(f"New mermaid code to write:\n{new_code}")

    return write_code(new_code)

PROMPT = """
You are a mermaid code generator. Generate mermaid instruction based on given instruction.
First use get_current_code to get current mermaid code.
Then update the code as per the instructions provided using write_to_current_code tool.
At the end return summary of changes made.
Your are not allow to ask for more information or clarification. At end write summary of what you have done.
"""

mermaid_generator_agent = create_agent(
    model=gemini_2_5_flash_lite,
    system_prompt=PROMPT,
    tools=[get_current_code, write_to_current_code]
)