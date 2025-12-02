from pydantic import BaseModel, Field
from typing_extensions import Literal

from langchain.agents import create_agent

from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite

class Route(BaseModel):
    next_agent: Literal["mermaid_validator", "planner", "requirements_gatherer", "mermaid_generator"] = Field(
        None, description="The next agent to callin the routing process"
    )
    instructions: str = Field(
        None, description="Instructions for the next agent"
    )


orchestrator_agent = create_agent(
    model=gemini_2_5_flash_lite,
    system_prompt="Choose appropriate agent to handle the request and provide instructions.",
    response_format=Route,
)