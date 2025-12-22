from pydantic import BaseModel, Field
from re import search
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite
from fastapi_lang_graph.core.logging import logger

search = DuckDuckGoSearchRun()

@tool
def search_on_duckduckgo(query: str) -> str:
    """Use this tool to search on DuckDuckGo."""
    logger.info("#############################")
    logger.info("search on duckduckgo function called")
    logger.info("#############################")

    # result = search.invoke(query)
    result = "web is down"

    logger.info(f"Search result:\n{result}")

    return result

PROMPT = """
You are a requirements gatherer agent.
1. Your task is to gather requirements based on user input related to mermaid.
2. Use the DuckDuckGo search tool if necessary to find relevant information.
3. A greeting (like hello, hi, how are you, etc.) then is_mermaid_related will be false.
"""

class Instructions(BaseModel):
    is_mermaid_related: bool = Field(
        description="Indicates if the query is related to mermaid diagrams"
    )
    instructions: str = Field(
        description="Instructions for the next agent"
    )

requirements_gatherer_agent = create_agent(
    model=gemini_2_5_flash_lite,
    system_prompt=PROMPT,
    tools=[search_on_duckduckgo],
    response_format=Instructions,
)