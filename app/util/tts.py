# Example with OpenAI TTS
from fastapi import Response
from openai import OpenAI
import requests

from app.core.config import env_config

async def speak_openai(text: str, gender: str):
    print("✅ gender value from DB:", repr(gender))
    payload = {
        "text": text,
        "language": "ko",
        "style": "neutral"
    }

    headers = {
        "x-sup-api-key": env_config.supertone_api_key,
        "Content-Type": "application/json"
    }

    # Supertone API 요청
    request_url = env_config.supertone_api_mok_url if gender == 'Mok-Sensei' else env_config.supertone_api_cindy_url
    res = requests.post(request_url, json=payload, headers=headers)

    if res.status_code != 200:
        return {"error": f"Supertone API failed: {res.status_code}", "detail": res.text}

    # 음성 파일이 바이너리 데이터로 온다고 가정
    audio_bytes = res.content

    return audio_bytes
