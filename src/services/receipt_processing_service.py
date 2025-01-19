
from uuid import uuid4
from src.models.receipt import Receipt

class ReceiptNotFound(Exception):
  pass

class ReceiptProcessingService():
  _receipts: dict = {}

  def __init__(self):
    self._receipts = {}

  def process_receipt(self, receipt: Receipt) -> str:
    new_id = str(uuid4())
    calculated_points = 0

    self._receipts[new_id] = calculated_points
    return new_id
  
  def get_points_for_receipt(self, id: str) -> int:
    if id in self._receipts:
      return self._receipts[id]
    
    raise ReceiptNotFound
