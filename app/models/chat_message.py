from sqlalchemy import Column, Integer, DateTime, Text
from datetime import datetime

from app.db.db import Base

class ChatMessage(Base):
    __tablename__ = "chat_message"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_room_id = Column(Integer, nullable=False)
    contents = Column(Text, nullable=False)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now, onupdate = datetime.now)