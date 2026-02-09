from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional
import uuid
from .base import Base
from enum import Enum

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskBaseFields:
    """Fields for Task model."""
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    priority: PriorityEnum = Field(default=PriorityEnum.medium)

def get_current_time():
    return datetime.utcnow()


def get_uuid():
    return str(uuid.uuid4())


from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.sql import func


class Task(TaskBaseFields, Base, table=True):
    """Task model representing a user's todo item."""
    __tablename__ = "tasks"

    id: str = Field(default=get_uuid, sa_column=Column(String, primary_key=True))
    user_id: str = Field(nullable=False)  # Foreign key to user
    created_at: datetime = Field(default=get_current_time, sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: datetime = Field(default=get_current_time, sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()))

    def __init__(self, **kwargs):
        # Generate ID if not provided
        if 'id' not in kwargs or not kwargs.get('id'):
            kwargs['id'] = get_uuid()
        # Set timestamps if not provided
        if 'created_at' not in kwargs or not kwargs.get('created_at'):
            kwargs['created_at'] = get_current_time()
        if 'updated_at' not in kwargs or not kwargs.get('updated_at'):
            kwargs['updated_at'] = get_current_time()
        super().__init__(**kwargs)

class TaskRead(TaskBaseFields, Base):
    """Schema for reading task data."""
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime

class TaskCreate(TaskBaseFields, Base):
    """Schema for creating a new task."""
    user_id: Optional[str] = None  # Will be set by the service to match the authenticated user

class TaskUpdate(SQLModel):
    """Schema for updating an existing task."""
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None