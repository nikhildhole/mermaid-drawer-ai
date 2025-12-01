from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def run_graph():
    return "Mermaid AI using FastAPI + LangChain Graph is up and running!"
