from fastapi import FastAPI

from text_processing_fast_api.api.v1 import router as v1_router
from text_processing_fast_api.core.di import db_engine


def start_fast_api():
    api = FastAPI(
        title="Async Text Processing API",
        description="""A simple web application that receives a text, saves it, and
        processes it asynchronously.
        """,
        version="0.1.0",
    )

    api.include_router(v1_router)

    ## Load models in database
    from text_processing_fast_api.models import load_database_tables

    load_database_tables(db_engine=db_engine)

    return api
