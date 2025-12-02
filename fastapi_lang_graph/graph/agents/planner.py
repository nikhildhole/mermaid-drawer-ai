from langchain.agents import create_agent
from langchain.tools import tool

from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite

PROMPT = """
You are a mermaid code writer agent planner. You can create plan and list of task to create or update mermaid code based on user query. There are following agents
1. mermaid generator agent which can read and write code
2. mermaid validator agent which can read and validate code
3. requirements gatherer agent which can gather requirements from internet based on user query
4. orchestrator agent which can decide which agent to call next based on current state of code and plan
5. summary generator agent which can generate summary of changes made to code
Based on user query create a plan and list of tasks to be performed by these agents in sequential order. Provide the plan and list of tasks as output.
"""

mermaid_validator_agent = create_agent(
    model=gemini_2_5_flash_lite,
    system_prompt=PROMPT,
)