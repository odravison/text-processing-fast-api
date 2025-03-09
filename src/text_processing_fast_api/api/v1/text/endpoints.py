from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.responses import JSONResponse
from text_processing_fast_api.models.user_request import UserRequest
from text_processing_fast_api.repositories.user_request import UserRequestRepository
from text_processing_fast_api.core.di import get_user_request_repository


router = APIRouter(prefix="/text")

user_request_repository = Annotated[UserRequestRepository, Depends(get_user_request_repository)]

@router.post(path="/")
async def create_new_text(
    body: dict,
    user_request_repository: user_request_repository
) -> JSONResponse:
    user_request: UserRequest = user_request_repository.add(
        UserRequest(
            body.get('text'),
        )
    )
    return JSONResponse(user_request.to_dict())