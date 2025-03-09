from typing import Callable
from sqlalchemy.orm import Session
from text_processing_fast_api.repositories.base import BaseRepository
from text_processing_fast_api.models.user_request import UserRequest

class UserRequestRepository(BaseRepository[UserRequest]):
    def __init__(self, get_session: Callable):
        super().__init__(get_session, UserRequest)
