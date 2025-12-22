from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from fastapi_lang_graph.graph.workflow import agent
from langchain.messages import HumanMessage
from pydantic import BaseModel
import json
import asyncio

from fastapi_lang_graph.core.logging import logger

router = APIRouter()

class AskRequest(BaseModel):
    query: str
    user_id: str

async def event_generator(query: str, user_id: str):
    """Generate SSE events from agent execution"""
    
    logger.info("-----------------------------------------------------------------------------------")
    logger.info("Starting new graph execution")
    logger.info("-----------------------------------------------------------------------------------")
    logger.info(f"User ID: {user_id}")
    logger.info(f"Received query: {query}")
    
    # Send initial event
    yield f"data: {json.dumps({'type': 'start', 'message': 'Starting agent workflow'})}\n\n"
    
    messages = [HumanMessage(content=query)]
    
    try:
        # Stream events from the agent using astream
        async for chunk in agent.astream(
            {"messages": messages, "user_id": user_id},
            stream_mode="updates"
        ):
            # Each chunk contains the node name and its output
            for node_name, node_output in chunk.items():
                logger.info(f"Node {node_name} completed")
                
                # Extract the result from the node output
                result_content = None
                if "messages" in node_output and node_output["messages"]:
                    # Get the last message content
                    last_message = node_output["messages"][-1]
                    result_content = last_message.content if hasattr(last_message, 'content') else str(last_message)
                
                data = {
                    "type": "agent_complete",
                    "agent": node_name,
                    "message": f"Completed {node_name.replace('_', ' ').title()}",
                    "result": result_content
                }
                yield f"data: {json.dumps(data)}\n\n"
                await asyncio.sleep(0)  # Allow other tasks to run
        
        # Send final completion event
        data = {
            "type": "complete",
            "message": "Workflow completed successfully"
        }
        yield f"data: {json.dumps(data)}\n\n"
        
    except Exception as e:
        logger.error(f"Error during graph execution: {str(e)}")
        error_data = {
            "type": "error",
            "message": str(e)
        }
        yield f"data: {json.dumps(error_data)}\n\n"

@router.post("/ask")
async def run_graph(request: AskRequest):
    """Endpoint to stream real-time updates from the agent graph"""
    return StreamingResponse(
        event_generator(request.query, request.user_id),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Disable buffering in nginx
        }
    )
