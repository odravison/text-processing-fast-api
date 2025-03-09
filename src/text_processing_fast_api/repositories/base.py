from sqlalchemy.orm import Session
from typing import Generic, TypeVar, Type
from text_processing_fast_api.models.base import Base

T = TypeVar("T", bound=Base)

class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get(self, id: int) -> T | None:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self):
        return self.db.query(self.model).all()

    def add(self, entity: T):
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def delete(self, id: int):
        entity = self.get(id)
        if entity:
            self.db.delete(entity)
            self.db.commit()
