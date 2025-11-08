from pydantic import BaseModel

class CreateChatMessageRequest(BaseModel):
    userId: int
    contents: str