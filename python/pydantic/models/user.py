from pydantic import Field
from uuid import uuid4

from models.base import MyBaseModel

class UserModel(MyBaseModel):
    public_id: str | None = Field(default_factory=lambda: f"user_{uuid4().hex}")
    name: str
    email: str
    phone: str
