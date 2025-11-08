from fastapi import APIRouter

from app.crud.s3_bucket import get_rag_documents

document_api = APIRouter(
    prefix="/documents",
    tags=["Document"]
)

@document_api.get("/{category}")
def index(category: str):
    urls = get_rag_documents(category)
    return {"status": 200, "message": urls}