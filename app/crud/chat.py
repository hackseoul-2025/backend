from app.db.db import connect_database
from app.models.character import Character
from app.models.chat_message import ChatMessage
from app.models.chat_room import ChatRoom
from app.models.create_chat_message_request import CreateChatMessageRequest
from app.models.create_chat_room_request import CreateChatRoomRequest
from app.crud.s3_bucket import get_class_image

def find_chat_messages(chat_room_id: int):
    with connect_database() as db:
        messages = db.query(ChatMessage).filter(ChatMessage.chat_room_id == chat_room_id).all()
        room = db.query(ChatRoom).filter(ChatRoom.id == chat_room_id).first()

    # 채팅방 이름을 기반으로 이미지 URL 생성
    image_url = get_class_image(room.name) if room else None

    # 각 메시지에 이미지 URL 추가
    result = []
    for message in messages:
        message_dict = {
            "id": message.id,
            "chat_room_id": message.chat_room_id,
            "user_id": message.user_id,
            "contents": message.contents,
            "created_at": message.created_at,
            "updated_at": message.updated_at,
            "image": image_url if message.user_id == None else None
        }
        result.append(message_dict)

    return result

def insert_chat_message(chat_room_id: int, request: CreateChatMessageRequest):
    message = ChatMessage(
        chat_room_id = chat_room_id,
        user_id = request.userId,
        contents = request.contents
    )

    with connect_database() as db:
        db.add(message)
        db.commit()
        db.refresh(message)

    return message

def insert_chat_room(user_id: int, request: CreateChatRoomRequest):
    chat_room = ChatRoom(
        user_id=user_id,
        location=request.location,
        name=request.name
    )

    with connect_database() as db:
        db.add(chat_room)
        db.commit()
        db.refresh(chat_room)

    return chat_room

def find_chat_rooms(user_id: int):
    with connect_database() as db:
        rooms = db.query(ChatRoom).filter(ChatRoom.user_id == user_id).all()

    # 각 메시지에 이미지 URL 추가
    result = []
    for room in rooms:
        image_url = get_class_image(room.name)
        room_dict = {
            "id":room.id,
            "user_id": room.user_id,
            "name": room.name,
            "location": room.location,
            "created_at": room.created_at,
            "updated_at": room.updated_at,
            "image": image_url
        }
        result.append(room_dict)

    return result

def find_chat_name_and_location(chat_room_id: int):
    with connect_database() as db:
        room = db.query(ChatRoom).filter(ChatRoom.id == chat_room_id).first()

    return { "name": room.name, "location": room.location }

def find_class_gender(chat_room_id: int):
    with connect_database() as db:
        name = find_chat_name_and_location(chat_room_id=chat_room_id)['name']
        return db.query(Character).filter(
            Character.class_name == name
        ).first()