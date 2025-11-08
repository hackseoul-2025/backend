from app.models.character import Character
from fastapi import FastAPI

from app.db.db import connect_database, engine, Base
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

DEFAULT_DATA = [
    {"class_name": "monalisa", "gender": "Cindy"},
    {"class_name": "bronze_mask", "gender": "Mok-Sensei"},
    {"class_name": "yongmiri_buddha", "gender": "Mok-Sensei"},
    {"class_name": "silsangsa", "gender": "Mok-Sensei"},
    {"class_name": "sundial", "gender": "Mok-Sensei"},
]

def init_seed_data():
    with connect_database() as db:
        for item in DEFAULT_DATA:
            exists = db.query(Character).filter(
                Character.class_name == item["class_name"]
            ).first()
            if not exists:
                db.add(Character(**item))
        db.commit()

@app.on_event("startup")
def on_startup():
    init_seed_data()

app.include_router(document_api, prefix = "/api/v1")
app.include_router(chat_api, prefix = "/api/v1")
app.include_router(model_api, prefix = "/api/v1")