
from fastapi_lang_graph.graph.agents.planner import planner_agent
from fastapi_lang_graph.core.logging import logger

def planner(state: dict):
    """Mermaid syntax generator"""

    logger.info("****************************")
    logger.info("planner node called")
    logger.info("****************************")

    messages = {"messages": state["messages"]}
    result = planner_agent.invoke(messages)

    logger.info(f"Planner output: {result.get('messages')[-1].content}")

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
    }