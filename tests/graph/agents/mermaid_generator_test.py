def test_orchestrator():
    from langchain_core.messages import AIMessage 
    from fastapi_lang_graph.graph.agents.mermaid_generator import mermaid_generator_agent

    response = mermaid_generator_agent.invoke({"messages": [{"role": "user", "content": "Draw a mermaid diagram for a simple A to B process."}]})
    assert isinstance(response, dict)
    assert isinstance(response.get("messages")[-1], AIMessage)
    assert isinstance(response.get("messages")[-1].content[0], str)

