from collections.abc import Callable

from text_processing_fast_api.models.user_request import UserRequest
from text_processing_fast_api.repositories.base import BaseRepository

user_request_factory = lambda **kwargs: UserRequest(**kwargs)  # noqa: E731


class UserRequestRepository(BaseRepository[UserRequest]):
    def __init__(self, get_session: Callable):
        super().__init__(get_session, UserRequest, user_request_factory)
