from fastapi import APIRouter, status

from app.crud.s3_bucket import find_yolo_model

model_api = APIRouter(
    prefix="/models",
    tags=["Model"]
)

@model_api.get("/{model_name}", status_code=status.HTTP_200_OK)
def get_yolo_model(model_name: str):
    return find_yolo_model(model_name=model_name)