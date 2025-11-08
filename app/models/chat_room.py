from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime

from app.db.db import Base

class ChatRoom(Base):
    __tablename__ = "chat_room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now, onupdate = datetime.now)