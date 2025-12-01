import uvicorn

def dev():
    uvicorn.run(
        "fastapi_lang_graph.main:app",
        reload=True,
        log_level="debug"
    )

def start():
    uvicorn.run("fastapi_lang_graph.main:app", reload=True)

def prod():
    uvicorn.run("fastapi_lang_graph.main:app", port=8000)
