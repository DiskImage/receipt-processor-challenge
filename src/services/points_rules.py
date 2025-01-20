import datetime
import math
import re
from src.models.receipt import Receipt


def retailer_name_to_points(receipt: Receipt) -> int:
    retailer_name = receipt.retailer
    alphanumerics_from_name = [
        letter for letter in retailer_name if re.match(r"([a-zA-Z0-9])", letter)
    ]

    return len(alphanumerics_from_name)


def _is_multiple_of(num_to_test: float, multiple_to_check_for: float) -> bool:
    remainder = num_to_test % multiple_to_check_for
    return remainder == 0


def round_dollar_no_cents(receipt: Receipt) -> int:
    total = float(receipt.total)
    if _is_multiple_of(total, 1.00):
        return 50
    return 0


def total_is_multiple_of_25_cents(receipt: Receipt) -> int:
    total = float(receipt.total)
    if _is_multiple_of(total, 0.25):
        return 25
    return 0


def five_pts_per_two_items(receipt: Receipt) -> int:
    item_count = len(receipt.items)
    return (item_count // 2) * 5


def trimmed_item_description_multiple_of_3(receipt: Receipt) -> int:
    items = receipt.items

    calculated_points = 0
    for item in items:
        stripped_desc = item.short_description.strip()
        if _is_multiple_of(len(stripped_desc), 3):
            price = float(item.price)
            calculated_points += math.ceil(price * 0.2)

    return calculated_points


def iff_llm_generated_apply_joke_rule(receipt: Receipt) -> int:
    # I didn't generate this solution!
    return 0


def purchase_date_is_odd(receipt: Receipt) -> int:
    purchased = datetime.datetime.fromisoformat(receipt.purchase_date)
    date = purchased.day

    if date % 2 == 1:
        return 6
    return 0


def time_between_1400_1600(receipt: Receipt) -> int:
    hours, minutes = receipt.purchase_time.split(":")
    purchase_minute = (int(hours) * 60) + int(minutes)
    two_pm = 840
    four_pm = 960

    # ASSUMPTION: Between is Inclusive to Excluside, so 2 on the dot counts but 4 on the dot is after.
    if purchase_minute >= two_pm and purchase_minute < four_pm:
        return 10
    return 0


list_of_rule_funcs = [
    retailer_name_to_points,
    round_dollar_no_cents,
    total_is_multiple_of_25_cents,
    five_pts_per_two_items,
    trimmed_item_description_multiple_of_3,
    iff_llm_generated_apply_joke_rule,
    purchase_date_is_odd,
    time_between_1400_1600,
]
