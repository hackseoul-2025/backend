from fastapi import APIRouter

test_api = APIRouter(
    prefix="/test",
    tags=["test"]
)

@test_api.post("/")
def index():
    return {"status": 200, "message": "hello world"}