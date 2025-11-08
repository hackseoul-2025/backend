from fastapi import APIRouter

from app.crud.chat import find_chat_messages

chat_api = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@chat_api.get("/{chat_room_id}")
def get_chat_messages(chat_room_id: int):
    messages = find_chat_messages(chat_room_id)
    return {"status": 200, "message": messages}