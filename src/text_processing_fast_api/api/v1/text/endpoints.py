from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.responses import JSONResponse

from text_processing_fast_api.api.v1.text.schemas import UserRequestSchema, UserRequestSchemaResponse
from text_processing_fast_api.core.di import (
    get_text_processing_service,
    get_user_request_repository,
)
from text_processing_fast_api.models.user_request import UserRequest
from text_processing_fast_api.repositories.user_request import UserRequestRepository
from text_processing_fast_api.services.text_processing import TextProcessingService

router = APIRouter(prefix="/text")

user_request_repository = Annotated[UserRequestRepository, Depends(get_user_request_repository)]
text_processing_service = Annotated[TextProcessingService, Depends(get_text_processing_service)]


@router.post(path="/")
async def create_new_text(
    body: UserRequestSchema,
    user_request_repository: user_request_repository,
    text_processing_service: text_processing_service,
    background_task: BackgroundTasks,
) -> JSONResponse:
    try:
        user_request: UserRequest = user_request_repository.add(
            UserRequest(
                **body.model_dump(),
            )
        )
        # user_request = UserRequestSchemaResponse.model_validate(user_request.to_dict())
        background_task.add_task(text_processing_service.process_text, user_request)
        return  UserRequestSchemaResponse.model_validate(user_request.to_dict()).model_dump_json()
    except Exception as e:
        print(type(e))
        return JSONResponse(status_code=400, content=dict(message=str(e)))
