"""
Schemas package for the Todo API.

This package contains all Pydantic schemas used for request/response validation
and data serialization/deserialization.
"""

# Import all schemas to make them available at the package level
from .task_schemas import (
    TaskBase,
    TaskCreate,
    TaskUpdate,
    TaskRead,
    TaskStatus,
    TaskToggleRequest,
    TaskToggleResponse,
    UserTasksResponse,
    SuccessResponse,
    ErrorResponse,
    HealthCheckResponse,
    TokenData,
    TokenResponse,
    PaginationParams,
    BatchOperationResponse
)

__all__ = [
    "TaskBase",
    "TaskCreate",
    "TaskUpdate",
    "TaskRead",
    "TaskStatus",
    "TaskToggleRequest",
    "TaskToggleResponse",
    "UserTasksResponse",
    "SuccessResponse",
    "ErrorResponse",
    "HealthCheckResponse",
    "TokenData",
    "TokenResponse",
    "PaginationParams",
    "BatchOperationResponse"
]