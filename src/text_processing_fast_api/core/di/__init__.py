from sqlalchemy import create_engine
from text_processing_fast_api.repositories.user_request import UserRequestRepository
from text_processing_fast_api.settings import get_settings
from sqlalchemy.orm import sessionmaker

settings = get_settings()

db_engine = create_engine(settings.db_dsn)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

user_request_repository = UserRequestRepository(
    SessionLocal()
)

async def get_user_request_repository():
    return user_request_repository