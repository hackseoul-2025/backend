from fastapi import APIRouter, status

from app.crud.chat import find_chat_messages, insert_chat_message, insert_chat_room, find_chat_rooms
from app.models.create_chat_message_request import CreateChatMessageRequest
from app.models.create_chat_room_request import CreateChatRoomRequest

chat_api = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@chat_api.get("/{chat_room_id}/messages", status_code=status.HTTP_200_OK)
def get_chat_messages(chat_room_id: int):
    messages = find_chat_messages(chat_room_id)
    return {"status": 200, "data": messages}

@chat_api.post("/{chat_room_id}/messages", status_code=status.HTTP_201_CREATED)
def create_chat_message(chat_room_id: int, request: CreateChatMessageRequest):
    response = insert_chat_message(chat_room_id=chat_room_id, request=request)
    # TODO: LLM Request and Response
    return {"status": 201, "data": response}

@chat_api.post("/{user_id}", status_code=status.HTTP_201_CREATED)
def create_chat_room(user_id: int, request: CreateChatRoomRequest):
    result = insert_chat_room(user_id, request=request)
    return {"status": 201, "data": {"result": result, "response": f"{request.name}(와)과의 즐거운 대화를 나눠보세요!"}}

@chat_api.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_chat_rooms(user_id: int):
    rooms = find_chat_rooms(user_id)
    return {"status": 200, "data": rooms}