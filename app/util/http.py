import requests

def call_llm_api_sync(request, question, room_id: int):
    resp = requests.post(
        "http://home.rocknroll17.com:8000/chat",
        json={
            "class_name": request["name"],
            "location": request["location"],
            "question": question,
            "room_id": room_id,
        },
        timeout=30
    )
    return resp.json()