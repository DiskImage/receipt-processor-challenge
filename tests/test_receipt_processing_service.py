from unittest.mock import patch
import pytest
from uuid import uuid4

from src.models.receipt import Receipt
from src.services.receipt_processing_service import ReceiptNotFound, ReceiptProcessingService


FIRST_MOCK_ID = "0aeb4aa8-6d78-4b90-92e7-af935afda512"
FIRST_EXAMPLE = {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}
FIRST_EXAMPLE_EXPECTED_POINTS = 28

SECOND_MOCK_ID = "045edd04-8a66-4ba1-bc54-757b7c1bdc3d"
SECOND_EXAMPLE = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
SECOND_EXAMPLE_EXPECTED_POINTS = 109



@pytest.mark.parametrize("mock_receipt_id,receipt_data,expected_points", [
  (FIRST_MOCK_ID, FIRST_EXAMPLE, FIRST_EXAMPLE_EXPECTED_POINTS),
  (SECOND_MOCK_ID, SECOND_EXAMPLE, SECOND_EXAMPLE_EXPECTED_POINTS)
])
@patch('src.services.receipt_processing_service.uuid4')
def test_get_points_for_receipt(mock_uuid4, mock_receipt_id: str, receipt_data: dict, expected_points: int):
  mock_uuid4.return_value = mock_receipt_id
  service = ReceiptProcessingService()

  receipt = Receipt.model_validate(receipt_data)
  service.process_receipt(receipt)
  try:
    result = service.get_points_for_receipt(mock_receipt_id)
  except ReceiptNotFound as e:
    raise e

  assert result == expected_points

def test_get_points_for_receipt_not_found():
  service = ReceiptProcessingService()
  id_to_find = str(uuid4())

  with pytest.raises(ReceiptNotFound):
    _unexpected_points = service.get_points_for_receipt(id=id_to_find)
