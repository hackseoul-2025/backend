from app.db.db import connect_database
from app.models.chat_message import ChatMessage
from app.models.chat_room import ChatRoom
from app.models.create_chat_message_request import CreateChatMessageRequest
from app.models.create_chat_room_request import CreateChatRoomRequest

def find_chat_messages(chat_room_id: int):
    with connect_database() as db:
        messages = db.query(ChatMessage).filter(ChatMessage.chat_room_id == chat_room_id).all()

    return messages

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

def insert_chat_room(request: CreateChatRoomRequest):
    chat_room = ChatRoom(
        user_id=1,
        name=request.name
    )

    with connect_database() as db:
        db.add(chat_room)
        db.commit()
        db.refresh(chat_room)

    return chat_room