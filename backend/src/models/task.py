from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional
from .base import Base


class TaskBase(Base):
    """Base class for Task with common fields."""
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    user_id: str  # This will come from JWT token, validated against URL parameter


class Task(TaskBase, table=True):
    """Task model representing a user's todo item."""
    __tablename__ = "tasks"

    id: Optional[str] = Field(default=None, primary_key=True)


class TaskRead(TaskBase):
    """Schema for reading task data."""
    id: str
    created_at: datetime
    updated_at: datetime


class TaskCreate(TaskBase):
    """Schema for creating a new task."""
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = False  # Default to False


class TaskUpdate(SQLModel):
    """Schema for updating an existing task."""
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = None