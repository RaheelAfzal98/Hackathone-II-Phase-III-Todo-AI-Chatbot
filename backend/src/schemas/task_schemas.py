from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    """Enum for task status values."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class TaskBase(BaseModel):
    """Base schema for task with common fields."""
    title: str = Field(..., min_length=1, max_length=200, description="Task title (1-200 characters)")
    description: Optional[str] = Field(None, max_length=1000, description="Optional task description (max 1000 characters)")
    completed: bool = Field(default=False, description="Whether the task is completed")


class TaskCreate(TaskBase):
    """Schema for creating a new task."""
    title: str = Field(..., min_length=1, max_length=200, description="Task title (1-200 characters)")
    # completed defaults to False when creating a new task
    completed: bool = False


class TaskUpdate(BaseModel):
    """Schema for updating an existing task."""
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Updated task title (1-200 characters)")
    description: Optional[str] = Field(None, max_length=1000, description="Updated task description (max 1000 characters)")
    completed: Optional[bool] = Field(None, description="Updated completion status")


class TaskRead(TaskBase):
    """Schema for reading task data with additional fields."""
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TaskToggleRequest(BaseModel):
    """Schema for toggling task completion status."""
    task_id: str


class TaskToggleResponse(BaseModel):
    """Schema for task toggle response."""
    id: str
    title: str
    completed: bool
    updated_at: datetime


class UserTasksResponse(BaseModel):
    """Schema for user tasks list response."""
    tasks: list[TaskRead]
    total_count: int


class SuccessResponse(BaseModel):
    """Generic success response schema."""
    success: bool = True
    message: str


class ErrorResponse(BaseModel):
    """Generic error response schema."""
    success: bool = False
    message: str
    error_code: Optional[str] = None


class HealthCheckResponse(BaseModel):
    """Schema for health check response."""
    status: str
    service: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class TokenData(BaseModel):
    """Schema for token data."""
    user_id: str
    exp: Optional[int] = None


class TokenResponse(BaseModel):
    """Schema for token response."""
    access_token: str
    token_type: str = "bearer"


class PaginationParams(BaseModel):
    """Schema for pagination parameters."""
    skip: int = Field(default=0, ge=0, description="Number of records to skip")
    limit: int = Field(default=100, ge=1, le=1000, description="Maximum number of records to return")


class BatchOperationResponse(BaseModel):
    """Schema for batch operation responses."""
    success_count: int
    failure_count: int
    total_count: int
    message: str