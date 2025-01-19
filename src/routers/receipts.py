from typing import Annotated
from fastapi import APIRouter, Request, Response, status, HTTPException
from pydantic import Field

from src.models.points_response import PointsResponse
from src.models.process_receipt_response import ProcessReceiptResponse
from src.models.receipt import Receipt
from src.services.receipt_processing_service import ReceiptNotFound, ReceiptProcessingService

router = APIRouter(prefix="/receipts")

BAD_REQUEST_MESSAGE = "The receipt is invalid."
NOT_FOUND_MESSAGE = "No receipt found for that ID."

processing_service = ReceiptProcessingService()

@router.post(
    path="/process",
    summary="Submits a receipt for processing.",
    description="Submits a receipt for processing.",
    response_model=ProcessReceiptResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": BAD_REQUEST_MESSAGE},
    },
)
def process_receipt(request: Request, receipt: Receipt):
    new_receipt_id = processing_service.process_receipt(receipt=receipt)
    return ProcessReceiptResponse(id=new_receipt_id)


@router.get(
    path="/receipts/{id}/points",
    summary="Returns the points awarded for the receipt.",
    description="Returns the points awarded for the receipt.",
    response_model=PointsResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"description": NOT_FOUND_MESSAGE},
    },
)
def get_receipt_points(
    id: Annotated[str, Field(pattern="^\\S+$", description="The ID of the receipt.")]
):
    try:
      points_found = processing_service.get_points_for_receipt(id=id)
    except ReceiptNotFound:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MESSAGE)
    return PointsResponse(points=points_found)
