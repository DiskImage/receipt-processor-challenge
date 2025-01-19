from fastapi import APIRouter
from .receipts import router as receipt_router

root_router = APIRouter()
root_router.include_router(receipt_router)
