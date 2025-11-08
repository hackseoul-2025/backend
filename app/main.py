from fastapi import FastAPI

from app.db.db import engine, Base
from app.api.documents import document_api

Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url = "/api/docs",
    openapi_url = "/api/openapi.json",
)

app.include_router(document_api, prefix = "/api/v1")