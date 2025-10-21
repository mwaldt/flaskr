from pydantic import Field
from pydantic import computed_field
from pydantic_extra_types.currency_code import ISO4217
from uuid import uuid4

from models.base import MyBaseModel


class ItemModel(MyBaseModel):
    public_id:  str | None = Field(default_factory=lambda: f"item_{uuid4().hex}")
    name: str
    description: str
    currency_code: ISO4217 = "USD"
    price_cents: int
    stock_quantity: int

    @computed_field
    @property
    def price(self) -> float:
        return self.price_cents / 100.0
