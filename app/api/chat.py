from fastapi import APIRouter

from app.crud.chat import find_chat_messages, insert_chat_message, insert_chat_room
from app.models.create_chat_message_request import CreateChatMessageRequest
from app.models.create_chat_room_request import CreateChatRoomRequest

chat_api = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@chat_api.get("/{chat_room_id}")
def get_chat_messages(chat_room_id: int):
    messages = find_chat_messages(chat_room_id)
    return {"status": 200, "message": messages}

@chat_api.post("/{chat_room_id}")
def create_chat_message(chat_room_id: int, request: CreateChatMessageRequest):
    response = insert_chat_message(chat_room_id=chat_room_id, request=request)
    # TODO: LLM Request and Response
    return {"status": 201, "message": response}

@chat_api.post("/")
def create_chat_room(request: CreateChatRoomRequest):
    result = insert_chat_room(request=request)
    return {"status": 201, "message": {"result": result, "response": f"{request.name}(와)과의 즐거운 대화를 나눠보세요!"}}