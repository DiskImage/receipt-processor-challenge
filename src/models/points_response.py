from typing import Annotated
from uuid import UUID
from pydantic import BaseModel, Field


class PointsResponse(BaseModel):
    points: Annotated[
        int, Field(description="The number of points awarded.", examples=[100])
    ]
