from fastapi_lang_graph.graph.agents.requirements_gatherer import requirements_gatherer_agent
from fastapi_lang_graph.core.logging import logger



def requirements_gatherer(state: dict):
    """Requirements gatherer"""

    logger.info("****************************")
    logger.info("requirements gatherer node called")
    logger.info("****************************")

    messages = {"messages": state["messages"]}
    result = requirements_gatherer_agent.invoke(messages)

    logger.info(f"Requirements gatherer output: {result.get('messages')[-1].content}")

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }