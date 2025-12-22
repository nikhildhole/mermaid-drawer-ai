from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from fastapi_lang_graph.api.v1.routers.graph import router as graph_router
from fastapi_lang_graph.api.v1.routers.working_test import router as working_test_router
from fastapi_lang_graph.api.v1.routers.mermaid import router as mermaid_router
from fastapi_lang_graph.services import code as code_service

app = FastAPI(title="FastAPI + LangChain Graph")

@app.on_event("startup")
async def startup_event():
    """Initialize event loop reference on startup"""
    loop = asyncio.get_running_loop()
    code_service.set_event_loop(loop)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # or specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Register routers
app.include_router(graph_router)
app.include_router(working_test_router)
app.include_router(mermaid_router)