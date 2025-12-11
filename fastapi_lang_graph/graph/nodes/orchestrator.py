from langchain_core.messages import AIMessage 

from fastapi_lang_graph.graph.agents.orchestrator import orchestrator_agent
from fastapi_lang_graph.core.logging import logger

def orchestrator(state: dict):
    """Orchestrator node to decide which agent to call next"""
    
    logger.info("****************************")
    logger.info("Orchestrator node called")
    logger.info("****************************")

    logger.info(f"Current state messages: {[msg.content for msg in state['messages']]}")

    # Invoke the orchestrator agent
    messages = {"messages": state["messages"]}
    agent_to_call = orchestrator_agent.invoke(messages)

    logger.info(f"Orchestrator decided to call: {agent_to_call.get('structured_response').next_agent}, with instructions: {agent_to_call.get('structured_response').instructions}")

    return {
        "messages": agent_to_call.get("messages") + [AIMessage(content=agent_to_call.get("structured_response").instructions)],
        "agent_to_call": agent_to_call.get("structured_response").next_agent,
        "agent_instructions": agent_to_call.get("structured_response").instructions,
        "llm_calls": state.get('llm_calls', 0) + 1,
    }

# Conditional edge function to route to the appropriate node
def route_decision(state: dict):
    # Return the node name you want to visit next
    if state["agent_to_call"] == "agent_to_call":
        return "mermaid_validator"
    elif state["agent_to_call"] == "planner":
        return "planner"
    elif state["agent_to_call"] == "requirements_analyzer":
        return "requirements_gatherer"
    elif state["agent_to_call"] == "mermaid_generator":
        return "mermaid_generator"
    elif state["agent_to_call"] == "summary_generator":
        return "summary_generator"
    else:
        raise ValueError(f"Unknown agent to call: {state['agent_to_call']}")