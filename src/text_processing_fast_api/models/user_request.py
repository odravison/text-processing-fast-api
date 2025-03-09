from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from text_processing_fast_api.models import Base

class UserRequest(Base):
    __tablename__ = "user_request"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    processed_text: Mapped[str] = mapped_column(String, nullable=True)

    def __init__(self, text: str, processed_text: str = None):
            self.text = text
            self.processed_text = processed_text

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}