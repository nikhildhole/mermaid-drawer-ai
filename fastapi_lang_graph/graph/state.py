from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator

class Task(TypedDict):
    title: str
    description: str

class MessagesState(TypedDict):
    llm_calls: int
    user_id: str
    user_query: str
    messages: Annotated[list[AnyMessage], operator.add]
    agent_to_call: str
    agent_instructions: str
    tasks: list[Task]
    is_mermaid_related: bool