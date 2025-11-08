from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import env_config

engine = create_engine(
    url = env_config.db_url,
    pool_pre_ping=True,    # 커넥션 유효성 검사
    pool_size = 5,    # database connection pool
    echo = True,     # SQLAlchemy가 실행하는 SQL 쿼리를 콘솔에 출력하도록 설정(개발 단계)
)

# 데이터베이스 접속을 위한 클래스, 연결을 통해 SQL 명령어를 실행
# 세션은 데이터베이스에 대한 트랜잭션 단위
SessionLocal = sessionmaker(
    autocommit = False,   # 트랜잭션이 자동으로 커밋되지 않도록 설정
    autoflush = False,   # 자동으로 데이터베이스에 변경 사항을 반영하지 않도록 설정
    bind = engine,
)

# 데이터베이스 모델 구성 시 사용, 데이터베이스 모델의 부모 클래스
# 해당 클래스를 상속받으면 SQLAlchemy가 자동으로 테이블과 매핑
Base = declarative_base()

@contextmanager
def connect_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()