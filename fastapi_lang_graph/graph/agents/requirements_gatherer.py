from re import search
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite

search = DuckDuckGoSearchRun()

@tool
def search_on_duckduckgo(query: str) -> str:
    """Use this tool to search on DuckDuckGo."""
    return search.invoke(query)

PROMPT = """
You are a requirements gatherer agent. Your task is to gather requirements based on user input related to mermaid. Use the DuckDuckGo search tool if necessary to find relevant information.
"""

requirements_gatherer_agent = create_agent(
    model=gemini_2_5_flash_lite,
    system_prompt=PROMPT,
    tools=[search_on_duckduckgo]
)