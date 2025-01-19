from fastapi import FastAPI
from src.routers import root_router


app = FastAPI(
    title="Receipt Processor",
    description="A simple receipt processor",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
)


app.include_router(root_router)
