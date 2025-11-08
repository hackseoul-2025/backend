from fastapi import APIRouter, status

from app.crud.s3_bucket import find_rag_documents

document_api = APIRouter(
    prefix="/documents",
    tags=["Document"]
)

@document_api.get("/{category}", status_code=status.HTTP_200_OK)
def get_rag_documents(category: str):
    urls = find_rag_documents(category)
    return {"status": 200, "message": urls}