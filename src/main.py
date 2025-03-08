from fastapi import FastAPI
from text_processing_fast_api.api.v1 import router as v1_router

def start_fast_api():
    api = FastAPI(
        title="Async Text Processing API",
        description="""A simple web application that receives a text, saves it and
        asynchronously processes it.
        """,
        version="0.1.0",
    )

    api.include_router(v1_router)

    return api