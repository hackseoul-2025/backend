from pydantic import Field   # env에 해당하는 값을 가져온다.
from pydantic_settings import BaseSettings
# 해당 모듈을 사용하면 dot_env 와 달리 타입 검증도 가능하다.

class EnvConfig(BaseSettings):
    # 변수명은 필드명과 같은 이름으로 해야 인식된다.
    db_url: str = Field(env='DB_URL')
    database: str = Field(env='DATABASE')
    db_password: str = Field(env='DB_PASSWORD')
    bucket_region: str = Field(env='BUCKET_REGION')
    bucket_access_key: str = Field(env='BUCKET_ACCESS_KEY')
    bucket_secret_key: str = Field(env='BUCKET_SECRET_KEY')
    bucket_name: str = Field(env='BUCKET_NAME')
    supertone_api_url: str = Field(env='SUPERTONE_API_URL')
    supertone_api_key: str = Field(env='SUPERTONE_API_KEY')

    class Config:
        env_file = ".env"

env_config = EnvConfig()