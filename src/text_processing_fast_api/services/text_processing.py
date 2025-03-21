import asyncio
import random

from text_processing_fast_api.models.user_request import UserRequest
from text_processing_fast_api.repositories.user_request import UserRequestRepository

words = ["banana", "Python", "fast", "API", "random", "text", "code", "developer"]


class TextProcessingService:
    user_request_repository: UserRequestRepository = None

    def __init__(self, user_request_repository: UserRequestRepository):
        self.user_request_repository = user_request_repository

    async def process_text(self, user_request_entity: UserRequest):
        print(f"Text received: {user_request_entity.text}", flush=True)
        await asyncio.sleep(random.randint(5, 10))
        processed_text: str = self._random_sentence(230)
        print("Text processed!", flush=True)
        user_request_entity.processed_text = processed_text
        self.user_request_repository.add(user_request_entity)
        print("Text saved!", flush=True)

    def _random_sentence(self, word_count=5):
        return " ".join(random.choices(words, k=word_count)) + "."
