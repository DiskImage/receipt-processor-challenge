from typing import Annotated
from pydantic import BaseModel, Field

from src.models.item import Item


class Receipt(BaseModel):
    retailer: Annotated[
        str,
        Field(
            pattern="^[\\w\\s\\-&]+$",
            description="The name of the retailer or store the receipt is from.",
            examples=["M&M Corner Market"],
        ),
    ]
    purchase_date: Annotated[
        str,
        Field(
            alias="purchaseDate",
            description="The date of the purchase printed on the receipt.",
            examples=["2022-01-01"],
        ),
    ]
    purchase_time: Annotated[
        str,
        Field(
            alias="purchaseDate",
            description="The time of the purchase printed on the receipt. 24-hour time expected.",
            examples=["13:01"],
        ),
    ]
    items: Annotated[list[Item], Field(min_length=1)]
    total: Annotated[
        str,
        Field(
            pattern="^\\d+\\.\\d{2}$",
            description="The total amount paid on the receipt.",
            examples=["6.49"],
        ),
    ]
