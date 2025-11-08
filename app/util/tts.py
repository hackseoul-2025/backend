# Example with OpenAI TTS
from fastapi import Response
from openai import OpenAI

from app.core.config import env_config

client = OpenAI(api_key=env_config.open_ai_key)

async def speak_openai(text: str):
    response = client.audio.speech.create(
        model="tts-1",
        voice="sage",
        input=text,
        response_format="wav"
    )
    audio_data = response.content
    
    return audio_data