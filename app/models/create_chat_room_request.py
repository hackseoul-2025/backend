from pydantic import BaseModel

class CreateChatRoomRequest(BaseModel):
    userId: int
    name: str