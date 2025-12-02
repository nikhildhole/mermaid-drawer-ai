def test_gemini_live_smoke():
    from langchain_core.messages import AIMessage 

    from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite

    response = gemini_2_5_flash_lite.invoke("Just and only say hi")
    assert isinstance(response, AIMessage)
    assert isinstance(response.content, str)
