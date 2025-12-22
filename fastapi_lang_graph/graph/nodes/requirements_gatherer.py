from fastapi_lang_graph.graph.agents.requirements_gatherer import requirements_gatherer_agent
from fastapi_lang_graph.core.logging import logger
from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite



def requirements_gatherer(state: dict):
    """Requirements gatherer"""

    logger.info("****************************")
    logger.info("requirements gatherer node called")
    logger.info("****************************")

    messages = {"messages": state["messages"]}
    
    messages = {"messages": state["messages"]}
    result = requirements_gatherer_agent.invoke(messages)

    logger.info(f"Requirements gatherer output: {result.get("structured_response").instructions}")
    result.get("messages").pop()  # Remove last message to avoid duplication in next steps
    result.get("messages").append(result.get("structured_response").instructions)

    return {
        "messages": result.get("messages"),
        "llm_calls": state.get('llm_calls', 0) + 1,
        "is_mermaid_related": result.get("structured_response").is_mermaid_related,
    }