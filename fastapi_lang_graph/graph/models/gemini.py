import os
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

gemini_2_5_flash_lite = init_chat_model("google_genai:gemini-2.5-flash-lite")
