from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/text")

@router.post(path="/")
async def create_new_text(body: dict) -> JSONResponse:
    return JSONResponse(body)