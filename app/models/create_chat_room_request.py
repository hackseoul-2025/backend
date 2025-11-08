from pydantic import BaseModel

class CreateChatRoomRequest(BaseModel):
    userId: int
    location: str
    name: str