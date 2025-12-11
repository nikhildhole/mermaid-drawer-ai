from langchain.agents import create_agent

from fastapi_lang_graph.graph.models.gemini import gemini_2_5_flash_lite


PROMPT = """
You are a summary generator. Generate summary based on other agent summarys. Be concise and clear.
"""

summary_generator_agent = create_agent(
    model=gemini_2_5_flash_lite,
    system_prompt=PROMPT,
)