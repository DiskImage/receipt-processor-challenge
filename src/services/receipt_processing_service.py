
from src.models.receipt import Receipt


class ReceiptProcessingService():
  _receipts: dict = {}

  def __init__(self):
    self._receipts = {}

  def process_receipt(self, receipt: Receipt) -> int:
    return 0
