from sqlalchemy.engine import Engine
from dependency_injector.wiring import Provide, inject
from text_processing_fast_api.models.base import Base
from text_processing_fast_api.models.user_request import UserRequest

@inject
def load_database_tables(db_engine: Provide[Engine]):
    print(db_engine)
    Base.metadata.create_all(db_engine)

__all__ = [
    'Base',
    'UserRequest',
    'load_database_tables'
]

