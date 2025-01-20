from uuid import uuid4

from fastapi import Request
from src.models.receipt import Receipt
from src.services.points_rules import list_of_rule_funcs


class ReceiptNotFound(Exception):
    pass


class ReceiptProcessingService:
    _receipts: dict = {}

    def __init__(self, receipts_to_points: dict = {}):
        self._receipts = receipts_to_points

    def process_receipt(self, receipt: Receipt) -> str:
        new_id = str(uuid4())
        calculated_points = 0

        rule_results = []
        for rule in list_of_rule_funcs:
            rule_result = rule(receipt)
            calculated_points += rule_result
            rule_results.append(rule_result)

        self._receipts[new_id] = calculated_points
        return new_id

    def get_points_for_receipt(self, id: str) -> int:
        if id in self._receipts:
            return self._receipts[id]

        raise ReceiptNotFound
