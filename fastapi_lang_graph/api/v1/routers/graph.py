from fastapi import APIRouter
from fastapi_lang_graph.graph.workflow import agent
from langchain.messages import HumanMessage
from pydantic import BaseModel

from fastapi_lang_graph.core.logging import logger

router = APIRouter()

class AskRequest(BaseModel):
    query: str

@router.post("/ask")
async def run_graph(request: AskRequest):
    """Endpoint to run the agent graph with a user query"""

    logger.info("-----------------------------------------------------------------------------------")
    logger.info("Starting new graph execution")
    logger.info("-----------------------------------------------------------------------------------")

    logger.info(f"Received query: {request.query}")
    
    messages = [HumanMessage(content=request.query)]
    messages = agent.invoke({"messages": messages})
    return messages["messages"][-1].content
