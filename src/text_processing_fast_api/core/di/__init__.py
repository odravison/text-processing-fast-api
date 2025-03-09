from contextlib import contextmanager
from sqlalchemy import create_engine
from text_processing_fast_api.repositories.user_request import UserRequestRepository
from text_processing_fast_api.services.text_processing import TextProcessingService
from text_processing_fast_api.settings import get_settings
from sqlalchemy.orm import sessionmaker

settings = get_settings()

db_engine = create_engine(settings.db_dsn)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()  # Try to commit the changes
    except Exception as e:
        db.rollback()  # Revert the changes in an exception
        print(f"Erro: {e}")
        raise
    finally:
        db.close()  # Close the connection

user_request_repository = UserRequestRepository(
    get_db
)

text_request_service = TextProcessingService(
    user_request_repository=user_request_repository
)

async def get_user_request_repository():
    return user_request_repository

async def get_text_processing_service():
    return text_request_service