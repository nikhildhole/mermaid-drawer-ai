from langgraph.graph import StateGraph, START, END

from fastapi_lang_graph.graph.state import MessagesState
from fastapi_lang_graph.graph.nodes.requirements_gatherer import requirements_gatherer
from fastapi_lang_graph.graph.nodes.mermaid_generator import mermaid_generator
from fastapi_lang_graph.graph.nodes.mermaid_validator import mermaid_validator
from fastapi_lang_graph.graph.nodes.summary_generator import summary_generator

# Define routing function
def route_after_requirements(state: MessagesState) -> str:
    """Route to mermaid_generator if query is mermaid-related, otherwise end."""
    if state.get("is_mermaid_related", True):
        return "mermaid_generator"
    return END

# Build workflow
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("requirements_gatherer", requirements_gatherer)
agent_builder.add_node("mermaid_generator", mermaid_generator)  
agent_builder.add_node("mermaid_validator", mermaid_validator)
agent_builder.add_node("summary_generator", summary_generator)

# Add edges
agent_builder.add_edge(START, "requirements_gatherer")
agent_builder.add_conditional_edges(
    "requirements_gatherer",
    route_after_requirements,
    {"mermaid_generator": "mermaid_generator", END: END}
)
agent_builder.add_edge("mermaid_generator", "mermaid_validator")
agent_builder.add_edge("mermaid_validator", "summary_generator")
agent_builder.add_edge("summary_generator", END)


# Compile the agent
agent = agent_builder.compile()