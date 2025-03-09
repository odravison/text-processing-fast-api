from sqlalchemy.orm import Session
from typing import Callable, Generic, TypeVar, Type
from text_processing_fast_api.models.base import Base

T = TypeVar("T", bound=Base)

class BaseRepository(Generic[T]):
    def __init__(self, get_session: Callable, model: Type[T]):
        self.get_session = get_session
        self.model = model

    def get(self, id: int) -> T | None:
        with self.get_session() as session:
            return session.query(self.model).filter(self.model.id == id).first()

    def get_all(self):
        with self.get_session() as session:
            return session.query(self.model).all()

    def add(self, entity: T):
        with self.get_session() as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity

    def delete(self, id: int):
        with self.get_session() as session:
            entity = self.get(id)
            if entity:
                session.delete(entity)
                session.commit()
