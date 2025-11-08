from fastapi import FastAPI

from app.db.db import engine, Base
from app.api.documents import document_api
from app.api.chat import chat_api
from app.api.model import model_api
from app.models.chat_message import ChatMessage
from app.models.chat_room import ChatRoom

Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url = "/api/docs",
    openapi_url = "/api/openapi.json",
)

app.include_router(document_api, prefix = "/api/v1")
app.include_router(chat_api, prefix = "/api/v1")
app.include_router(model_api, prefix = "/api/v1")