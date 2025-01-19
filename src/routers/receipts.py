from typing import Annotated
from fastapi import APIRouter, Request, Response, status, HTTPException
from pydantic import Field

from src.models.points_response import PointsResponse
from src.models.process_receipt_response import ProcessReceiptResponse
from src.models.receipt import Receipt

router = APIRouter(prefix="/receipts")

BAD_REQUEST_MESSAGE = "The receipt is invalid."
NOT_FOUND_MESSAGE = "No receipt found for that ID."


@router.post(
    path="/process",
    summary="Submits a receipt for processing.",
    description="Submits a receipt for processing.",
    response_model=ProcessReceiptResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": BAD_REQUEST_MESSAGE},
    },
)
async def process_receipt(request: Request, receipt: Receipt):
    return Response(status_code=status.HTTP_200_OK)


@router.get(
    path="/receipts/{id}/points",
    summary="Returns the points awarded for the receipt.",
    description="Returns the points awarded for the receipt.",
    response_model=PointsResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"description": NOT_FOUND_MESSAGE},
    },
)
async def get_receipt_points(
    id: Annotated[str, Field(pattern="^\\S+$", description="The ID of the receipt.")]
):
    return Response(status_code=status.HTTP_200_OK)
