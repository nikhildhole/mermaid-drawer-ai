def test_orchestrator():
    from fastapi_lang_graph.graph.agents.orchestrator import orchestrator_agent, Route

    response = orchestrator_agent.invoke({"messages": [{"role": "user", "content": "Draw a mermaid diagram for a simple web app."}]})
    assert isinstance(response, dict)
    assert isinstance(response.get("structured_response"), Route)
    assert isinstance(response.get("structured_response").next_agent, str)
    assert response.get("structured_response").next_agent == "mermaid_generator"
