from sqlmodel import SQLModel
from datetime import datetime
from typing import Optional
import uuid


class Base(SQLModel):
    """Base model with common fields for all entities."""
    pass