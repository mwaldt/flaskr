from pydantic import Field
from models.base import MyBaseModel
from uuid import uuid4


class AddressModel(MyBaseModel):
    public_id:  str | None = Field(default_factory=lambda: f"addr_{uuid4().hex}")
    street1: str
    street2: str
    city: str
    state: str
    postal_code: str
    country: str
