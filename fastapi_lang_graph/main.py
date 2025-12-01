from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_lang_graph.api.v1.routers.graph import router as graph_router
from fastapi_lang_graph.api.v1.routers.working_test import router as working_test_router

app = FastAPI(title="FastAPI + LangChain Graph")
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