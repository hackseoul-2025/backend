from app.db.db import connect_database
from app.models.chat_message import ChatMessage

def find_chat_messages(chat_room_id: int):
    with connect_database() as db:
        messages = db.query(ChatMessage).filter(ChatMessage.chat_room_id == chat_room_id).all()

    return messages
