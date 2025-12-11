
from fastapi_lang_graph.graph.agents.mermaid_validator import mermaid_validator_agent
from fastapi_lang_graph.core.logging import logger

def mermaid_validator(state: dict):
    """Mermaid syntax validator"""

    logger.info("****************************")
    logger.info("mermaid validator node called")
    logger.info("****************************")

    messages = {"messages": state["messages"]}
    result = mermaid_validator_agent.invoke(messages)

    logger.info(f"Mermaid validator output: {result.get('messages')[-1].content}")

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }