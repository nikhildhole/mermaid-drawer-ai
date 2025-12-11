from fastapi import APIRouter
from fastapi_lang_graph.core.logging import logger

router = APIRouter()


@router.get("/")
async def run_graph():

    logger.info("-----------------------------------------------------------------------------------")
    logger.info(f"Health check endpoint called")
    logger.info("-----------------------------------------------------------------------------------")
    
    return "Mermaid AI using FastAPI + LangChain Graph is up and running!"
