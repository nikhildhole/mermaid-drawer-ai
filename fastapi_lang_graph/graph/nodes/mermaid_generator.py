
from fastapi_lang_graph.graph.agents.mermaid_generator import mermaid_generator_agent
from fastapi_lang_graph.core.logging import logger


def mermaid_generator(state: dict):
    """Mermaid syntax generator"""

    logger.info("****************************")
    logger.info("mermaid generator node called")
    logger.info("****************************")

    logger.info(f"Current state messages: {[msg.content for msg in state['messages']]}")

    messages = {"messages": state["messages"]}
    result = mermaid_generator_agent.invoke(messages)

    logger.info(f"Mermaid generator output: {result.get('messages')[-1].content}")

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }