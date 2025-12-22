
from fastapi_lang_graph.graph.agents.mermaid_generator import mermaid_generator_agent, current_user_id
from fastapi_lang_graph.core.logging import logger


def mermaid_generator(state: dict):
    """Mermaid syntax generator"""

    logger.info("****************************")
    logger.info("mermaid generator node called")
    logger.info("****************************")


    # Set the user_id in context for tools to access
    user_id = state.get('user_id', '')
    current_user_id.set(user_id)
    logger.info(f"Processing for user_id: {user_id}")

    messages = {"messages": state["messages"]}
    result = mermaid_generator_agent.invoke(messages)

    logger.info(f"Mermaid generator output: {result.get('messages')[-1].content}")

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }