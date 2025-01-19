from typing import Annotated
from uuid import UUID
from pydantic import BaseModel, Field


class ProcessReceiptResponse(BaseModel):
    id: Annotated[UUID, Field(examples=["adb6b560-0eef-42bc-9d16-df48f30e89b2"])]
