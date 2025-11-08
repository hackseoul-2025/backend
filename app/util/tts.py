# Example with OpenAI TTS
from fastapi import Response
from openai import OpenAI
import requests

from app.core.config import env_config

async def speak_openai(text: str):
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
    res = requests.post(env_config.supertone_api_url, json=payload, headers=headers)

    if res.status_code != 200:
        return {"error": f"Supertone API failed: {res.status_code}", "detail": res.text}

    # 음성 파일이 바이너리 데이터로 온다고 가정
    audio_bytes = res.content

    return audio_bytes
