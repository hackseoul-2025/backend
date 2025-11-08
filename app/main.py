from fastapi import FastAPI

from app.db.db import engine, Base
from app.api.test import test_api

Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url = "/api/docs",
    openapi_url = "/api/openapi.json",
)

app.include_router(test_api, prefix = "/api/v1")