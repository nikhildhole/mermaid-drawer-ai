from langchain.messages import SystemMessage
from fastapi_lang_graph.graph.models.gemini import gemini

from enum import Enum
from pydantic import BaseModel, Field

from fastapi_lang_graph.core.logging import logger

class Agents(str, Enum):
    MERMAID_VALIDATOR = "mermaid_validator"
    PLANNER = "planner"
    REQUIREMENTS_ANALYZER = "requirements_analyzer"
    MERMAID_GENERATOR = "mermaid_generator"


class Agent(BaseModel):
    agent: Agents = Field(description="The phone number of the person")


prompt = """
Choose appropriate agent to handle the following user request and past interactions.
"""


def orchestrator(state: dict):
    """Orchestrator node to decide which agent to call next"""
    logger.info("Orchestrator invoked")
    logger.debug(f"Current state: {state}")

    orchestrator_agent = gemini.with_structured_output(Agent)

    messages = [
                    SystemMessage(
                        content=prompt
                    )
                ] + state["messages"]
    logger.debug(f"Messages sent to agent: {messages}")
    agent_to_call = orchestrator_agent.invoke(messages)
    logger.debug(f"Agent to call: {agent_to_call}")
    return {
        "agent_to_call": agent_to_call.agent,
        "llm_calls": state.get('llm_calls', 0) + 1,
    }

# Conditional edge function to route to the appropriate node
def route_decision(state: dict):
    # Return the node name you want to visit next
    if state["agent_to_call"] == Agents.MERMAID_VALIDATOR:
        return "mermaid_validator"
    elif state["agent_to_call"] == Agents.PLANNER:
        return "planner"
    elif state["agent_to_call"] == Agents.REQUIREMENTS_ANALYZER:
        return "requirements_gatherer"
    elif state["agent_to_call"] == Agents.MERMAID_GENERATOR:
        return "mermaid_generator"
    else:
        raise ValueError(f"Unknown agent to call: {state['agent_to_call']}")