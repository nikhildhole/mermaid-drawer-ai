from langgraph.graph import StateGraph, START, END

from fastapi_lang_graph.graph.state import MessagesState
from fastapi_lang_graph.graph.nodes.llm_call import llm_call
from fastapi_lang_graph.graph.nodes.orchestrator import orchestrator, route_decision
from fastapi_lang_graph.graph.nodes.requirements_gatherer import requirements_gatherer
from fastapi_lang_graph.graph.nodes.planner import planner
from fastapi_lang_graph.graph.nodes.mermaid_generator import mermaid_generator
from fastapi_lang_graph.graph.nodes.mermaid_validator import mermaid_validator
from fastapi_lang_graph.graph.nodes.summary_generator import summary_generator

# Build workflow
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("orchestrator", orchestrator)
agent_builder.add_node("requirements_gatherer", requirements_gatherer)
agent_builder.add_node("planner", planner)
agent_builder.add_node("mermaid_generator", mermaid_generator)  
agent_builder.add_node("mermaid_validator", mermaid_validator)
agent_builder.add_node("summary_generator", summary_generator)


# Add edges to connect nodes
agent_builder.add_edge(START, "orchestrator")
agent_builder.add_conditional_edges(
    "orchestrator",
    route_decision,
    {  # Name returned by route_decision : Name of next node to visit
        "mermaid_validator": "mermaid_validator",
        "planner": "planner",
        "requirements_gatherer": "requirements_gatherer",
        "mermaid_generator": "mermaid_generator",
    },
)
agent_builder.add_edge("mermaid_validator", "orchestrator")
agent_builder.add_edge("planner", "orchestrator")
agent_builder.add_edge("requirements_gatherer", "orchestrator")
agent_builder.add_edge("mermaid_generator", "orchestrator")
agent_builder.add_edge("summary_generator", END)


# Compile the agent
agent = agent_builder.compile()

# # Invoke
# from langchain.messages import HumanMessage
# messages = [HumanMessage(content="Add 3 and 4.")]
# messages = agent.invoke({"messages": messages})
# for m in messages["messages"]:
#     m.pretty_print()