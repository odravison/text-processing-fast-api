from pydantic import BaseModel

class UserRequestSchemaResponse(BaseModel):
    id: int
    text: str
    processed_text: str | None

    class Config:
        from_attributes = True

from pydantic import BaseModel

class UserRequestSchema(BaseModel):
    text: str
