from pydantic import Field   # env에 해당하는 값을 가져온다.
from pydantic_settings import BaseSettings
# 해당 모듈을 사용하면 dot_env 와 달리 타입 검증도 가능하다.

class EnvConfig(BaseSettings):
    # 변수명은 필드명과 같은 이름으로 해야 인식된다.
    db_url: str = Field(env='DB_URL')

    class Config:
        env_file = ".env"

env_config = EnvConfig()