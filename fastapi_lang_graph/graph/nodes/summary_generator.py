from fastapi_lang_graph.graph.agents.summary_generator import summary_generator_agent
from fastapi_lang_graph.core.logging import logger


def summary_generator(state: dict):
    """Summary generator"""

    logger.info("****************************")
    logger.info("summary generator node called")
    logger.info("****************************")

    messages = {"messages": state["messages"]}
    result = summary_generator_agent.invoke(messages)

    logger.info(f"Summary generator output: {result.get('messages')[-1].content}")

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }