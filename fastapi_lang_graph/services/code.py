"""Service for managing mermaid code storage per user."""
import asyncio
from fastapi_lang_graph.core.logging import logger

# Store reference to main event loop
_main_loop = None

def set_event_loop(loop):
    """Set the main event loop reference."""
    global _main_loop
    _main_loop = loop

# Import the user storage from mermaid router
# This will be a reference to the same dictionary
def get_user_storage():
    """Get reference to user mermaid storage."""
    from fastapi_lang_graph.api.v1.routers.mermaid import user_mermaid_storage
    return user_mermaid_storage

def get_websocket_manager():
    """Get reference to websocket connection manager."""
    from fastapi_lang_graph.api.v1.routers.mermaid import manager
    return manager

def get_code(user_id: str) -> str:
    """
    Get the current mermaid code for a specific user.
    
    Args:
        user_id: The user identifier
        
    Returns:
        The mermaid code string for the user, or empty string if none exists
    """
    storage = get_user_storage()
    user_data = storage.get(user_id, {"content": ""})
    code = user_data.get("content", "")
    
    logger.info(f"Retrieved mermaid code for user {user_id}: {len(code)} characters")
    
    return code

def write_code(user_id: str, new_code: str) -> bool:
    """
    Write/update the mermaid code for a specific user and send via websocket.
    
    Args:
        user_id: The user identifier
        new_code: The new mermaid code to store
        
    Returns:
        True if successful
    """
    storage = get_user_storage()
    storage[user_id] = {"content": new_code}
    
    logger.info(f"Wrote mermaid code for user {user_id}: {len(new_code)} characters")
    
    # Send update via websocket
    manager = get_websocket_manager()
    try:
        # Try to get running loop, otherwise use stored main loop
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = _main_loop
        
        if loop is not None:
            asyncio.run_coroutine_threadsafe(
                manager.send_to_user(user_id, {
                    "type": "code_updated",
                    "content": new_code,
                    "user_id": user_id
                }),
                loop
            )
            logger.info(f"Sent websocket update for user {user_id}")
        else:
            logger.warning("No event loop available for websocket update")
    except Exception as e:
        logger.error(f"Failed to send websocket update: {e}")
    
    return True
