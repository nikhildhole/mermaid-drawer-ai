def test_requirements_gatherer():
    from langchain_core.messages import AIMessage 
    from fastapi_lang_graph.graph.agents.requirements_gatherer import requirements_gatherer_agent

    response = requirements_gatherer_agent.invoke({"messages": [{"role": "user", "content": "Draw a mermaid diagram for a simple A to B process."}]})
    assert isinstance(response, dict)
    assert isinstance(response.get("messages")[-1], AIMessage)
    assert isinstance(response.get("messages")[-1].content[0], str)


def test_search_on_duckduckgo():
    from fastapi_lang_graph.graph.agents.requirements_gatherer import search_on_duckduckgo
    result = search_on_duckduckgo.run("Capital of india")
    print(result)
    assert "Delhi" in result