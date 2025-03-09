from sqlalchemy.orm import Session
from text_processing_fast_api.repositories.base import BaseRepository
from text_processing_fast_api.models.user_request import UserRequest

class UserRequestRepository(BaseRepository[UserRequest]):
    def __init__(self, db: Session):
        super().__init__(db, UserRequest)
