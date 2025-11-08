from sqlalchemy import Column, Integer, String
from app.db.db import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String(255), unique=True, index=True, nullable=False)
    gender = Column(String(255), nullable=False)
