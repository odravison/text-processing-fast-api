from fastapi import APIRouter

from text_processing_fast_api.api.v1.text.endpoints import router as text_router

router = APIRouter(prefix="/v1")
router.include_router(text_router)
