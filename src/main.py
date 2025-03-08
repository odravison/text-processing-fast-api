from fastapi import FastAPI

async def start_fast_api():
    api = FastAPI(
        title="Async Text Processing API",
        description="""A simple web application that receives a text, saves it and
        asynchronously processes it.
        """,
        version="0.1.0",
    )

    return api