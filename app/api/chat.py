from app.crud.s3_bucket import find_audio_tts, get_class_image
from app.util.tts import speak_openai
from fastapi import APIRouter, status

from app.crud.chat import find_chat_messages, find_chat_name_and_location, find_class_gender, insert_chat_message, insert_chat_room, find_chat_rooms
from app.util.http import call_llm_api_sync
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
async def create_chat_message(chat_room_id: int, request: CreateChatMessageRequest):
    response = insert_chat_message(chat_room_id=chat_room_id, request=request)
    llm_request = find_chat_name_and_location(chat_room_id=chat_room_id)
    llm_response = call_llm_api_sync(llm_request, question=request.contents, room_id=chat_room_id)
    request.userId = None
    request.contents = llm_response.get("response")
    response = insert_chat_message(chat_room_id=chat_room_id, request=request)
    # 클래스명 기반 성별 찾기
    gender = find_class_gender(chat_room_id).gender
    tts_result = await speak_openai(request.contents, gender)
    tts_url = find_audio_tts(tts_result)
    return {"status": 201, "data": {"message": response, "audio": tts_url}}

@chat_api.post("/{user_id}", status_code=status.HTTP_201_CREATED)
def create_chat_room(user_id: int, request: CreateChatRoomRequest):
    result = insert_chat_room(user_id, request=request)
    return {"status": 201, "data": {"result": result, "response": f"{request.name}(와)과의 즐거운 대화를 나눠보세요!"}}

@chat_api.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_chat_rooms(user_id: int):
    rooms = find_chat_rooms(user_id)
    return {"status": 200, "data": rooms}

@chat_api.get("/{chat_room_id}/images", status_code=status.HTTP_200_OK)
def get_chat_rooms(chat_room_id: int, name: str):
    url = get_class_image(name)
    return {"status": 200, "data": url}