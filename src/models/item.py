from typing import Annotated
from pydantic import BaseModel, Field


class Item(BaseModel):
    short_description: Annotated[
        str,
        Field(
            alias="shortDescription",
            pattern="^[\\w\\s\\-]+$",
            description="The Short Product Description for the item.",
            examples=["Mountain Dew 12PK"],
        ),
    ]
    price: Annotated[
        str,
        Field(
            pattern="^\\d+\\.\\d{2}$",
            description="The total price payed for this item.",
            examples=["6.49"],
        ),
    ]
