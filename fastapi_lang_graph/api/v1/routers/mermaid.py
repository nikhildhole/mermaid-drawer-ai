from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

from fastapi_lang_graph.core.logging import logger

router = APIRouter()

# Storage for mermaid text per user
# Format: {user_id: {"content": "mermaid_text"}}
user_mermaid_storage = {}
class ConnectionManager:
    def __init__(self):
        # Store active connections per user_id
        self.active_connections: dict[str, list[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = []
        self.active_connections[user_id].append(websocket)
        logger.info(f"WebSocket connected for user {user_id}. Total connections: {len(self.active_connections[user_id])}")
    
    def disconnect(self, websocket: WebSocket, user_id: str):
        if user_id in self.active_connections:
            if websocket in self.active_connections[user_id]:
                self.active_connections[user_id].remove(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]
        logger.info(f"WebSocket disconnected for user {user_id}")
    
    async def send_to_user(self, user_id: str, message: dict):
        """Send message to all connections for a specific user"""
        if user_id in self.active_connections:
            disconnected = []
            for connection in self.active_connections[user_id]:
                try:
                    await connection.send_json(message)
                except Exception as e:
                    logger.error(f"Error sending to websocket: {e}")
                    disconnected.append(connection)
            
            # Remove disconnected websockets
            for conn in disconnected:
                self.disconnect(conn, user_id)

manager = ConnectionManager()

@router.websocket("/mermaid")
async def websocket_mermaid(websocket: WebSocket):
    """WebSocket endpoint to store and retrieve mermaid text per user"""
    await websocket.accept()
    logger.info("WebSocket connection accepted for mermaid endpoint")
    user_id = None
    
    try:
        while True:
            # Receive data from client
            data = await websocket.receive_json()
            received_user_id = data.get("user_id")
            
            if not received_user_id:
                await websocket.send_json({
                    "type": "error",
                    "message": "user_id is required"
                })
                continue
            
            # Register connection on first message
            if user_id is None:
                user_id = received_user_id
                if user_id not in manager.active_connections:
                    manager.active_connections[user_id] = []
                manager.active_connections[user_id].append(websocket)
                logger.info(f"WebSocket registered for user {user_id}. Total connections: {len(manager.active_connections[user_id])}")
            
            if data.get("type") == "update":
                # Store the mermaid text for this user
                content = data.get("content", "")
                user_mermaid_storage[user_id] = {"content": content}
                logger.info(f"Updated mermaid text for user {user_id} ({len(content)} characters)")
                logger.info(f"\n{content}")
                
                # Acknowledge the update
                await websocket.send_json({
                    "type": "acknowledged",
                    "message": "Mermaid text updated successfully",
                    "user_id": user_id
                })
            
            elif data.get("type") == "get":
                # Send current mermaid text for this user
                user_data = user_mermaid_storage.get(user_id, {"content": ""})
                await websocket.send_json({
                    "type": "current",
                    "content": user_data["content"],
                    "user_id": user_id
                })
    
    except WebSocketDisconnect:
        logger.info("WebSocket connection closed for mermaid endpoint")
        if user_id:
            manager.disconnect(websocket, user_id)
    except Exception as e:
        logger.error(f"Error in mermaid WebSocket: {str(e)}")
        if user_id:
            manager.disconnect(websocket, user_id)
        try:
            await websocket.close()
        except:
            pass