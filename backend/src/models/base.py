from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid


class Base(SQLModel):
    """Base model with common fields for all entities."""

    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    def __setattr__(self, name, value):
        """Override to automatically update updated_at field when any attribute changes."""
        if name != "updated_at":
            super().__setattr__("updated_at", datetime.utcnow())
        super().__setattr__(name, value)