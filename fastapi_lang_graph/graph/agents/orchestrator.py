from langchain.agents import create_agent

from fastapi_lang_graph.graph.models.gemini import gemini_model

orchestrator_agent = create_agent(
    model="anthropic:claude-sonnet-4-5-20250929",
    tools=[check_weather],
    system_prompt="You are a helpful assistant",
)