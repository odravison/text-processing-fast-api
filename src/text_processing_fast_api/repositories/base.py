from sqlalchemy import update
from collections.abc import Callable
from typing import Generic, TypeVar

from text_processing_fast_api.models.base import Base

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    def __init__(self, get_session: Callable, model: type[T], model_factory: Callable[[], T]):
        self.get_session = get_session
        self.model = model
        self.model_factory = model_factory

    def _create_instance(self, **kwargs) -> T:
        return self.model_factory(**kwargs)

    def get(self, id: int) -> T | None:
        with self.get_session() as session:
            entity = session.query(self.model).filter(self.model.id == id).first()
            return self._create_instance(**entity.to_dict()) if entity else None

    def get_all(self) -> list[T]:
        with self.get_session() as session:
            return [
                self._create_instance(**entity.to_dict())
                for entity in session.query(self.model).all()
            ]

    def add(self, entity: T) -> T:
        with self.get_session() as session:
            if entity.id:
                session.execute(
                    update(self.model),
                    [
                        entity.to_dict()
                    ]
                )
                session.commit()
            else:
                session.add(entity)
                session.commit()
                session.refresh(entity)
            return self._create_instance(**entity.to_dict())

    def delete(self, id: int):
        with self.get_session() as session:
            entity = self.get(id)
            if entity:
                session.delete(entity)
                session.commit()
