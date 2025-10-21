import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4


class MyBaseModel(BaseModel):
    public_id: str | None = Field(default_factory=lambda: f"obj_{uuid4().hex}")
    created_at: str | None = datetime.datetime.now(datetime.UTC).isoformat()
    updated_at: str | None = datetime.datetime.now(datetime.UTC).isoformat()
