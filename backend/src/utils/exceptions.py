from typing import Optional
from fastapi import HTTPException, status


class BaseCustomException(Exception):
    """Base exception class for custom application exceptions."""

    def __init__(self, message: str, error_code: Optional[str] = None, details: Optional[dict] = None):
        self.message = message
        self.error_code = error_code or self.__class__.__name__
        self.details = details or {}
        super().__init__(self.message)

    def __str__(self):
        return f"{self.error_code}: {self.message}"


class TaskNotFoundException(BaseCustomException):
    """Raised when a task is not found."""

    def __init__(self, task_id: str, user_id: str, details: Optional[dict] = None):
        message = f"Task with ID '{task_id}' not found for user '{user_id}'"
        error_code = "TASK_NOT_FOUND"
        super().__init__(message, error_code, details)


class UserUnauthorizedException(BaseCustomException):
    """Raised when a user is not authorized to perform an action."""

    def __init__(self, message: str = "User not authorized to perform this action", details: Optional[dict] = None):
        error_code = "USER_UNAUTHORIZED"
        super().__init__(message, error_code, details)


class InvalidTokenException(BaseCustomException):
    """Raised when a JWT token is invalid or expired."""

    def __init__(self, message: str = "Invalid or expired token", details: Optional[dict] = None):
        error_code = "INVALID_TOKEN"
        super().__init__(message, error_code, details)


class TaskValidationException(BaseCustomException):
    """Raised when task data fails validation."""

    def __init__(self, message: str, details: Optional[dict] = None):
        error_code = "TASK_VALIDATION_ERROR"
        super().__init__(message, error_code, details)


class DatabaseConnectionException(BaseCustomException):
    """Raised when there's an issue connecting to the database."""

    def __init__(self, message: str = "Database connection error", details: Optional[dict] = None):
        error_code = "DATABASE_CONNECTION_ERROR"
        super().__init__(message, error_code, details)


class DuplicateTaskException(BaseCustomException):
    """Raised when trying to create a duplicate task."""

    def __init__(self, message: str = "Task already exists", details: Optional[dict] = None):
        error_code = "DUPLICATE_TASK_ERROR"
        super().__init__(message, error_code, details)


def create_http_exception(
    status_code: int,
    detail: str,
    headers: Optional[dict] = None
) -> HTTPException:
    """
    Helper function to create HTTPException with consistent formatting.

    Args:
        status_code (int): HTTP status code
        detail (str): Error detail message
        headers (Optional[dict]): Optional headers to include

    Returns:
        HTTPException: FastAPI HTTPException instance
    """
    return HTTPException(
        status_code=status_code,
        detail=detail,
        headers=headers
    )


def create_unauthorized_exception(detail: str = "Not authenticated") -> HTTPException:
    """
    Helper function to create unauthorized HTTPException.

    Args:
        detail (str): Error detail message

    Returns:
        HTTPException: FastAPI HTTPException instance with 401 status
    """
    return create_http_exception(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail
    )


def create_forbidden_exception(detail: str = "Access denied") -> HTTPException:
    """
    Helper function to create forbidden HTTPException.

    Args:
        detail (str): Error detail message

    Returns:
        HTTPException: FastAPI HTTPException instance with 403 status
    """
    return create_http_exception(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=detail
    )


def create_not_found_exception(detail: str = "Item not found") -> HTTPException:
    """
    Helper function to create not found HTTPException.

    Args:
        detail (str): Error detail message

    Returns:
        HTTPException: FastAPI HTTPException instance with 404 status
    """
    return create_http_exception(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail
    )


def create_validation_exception(detail: str = "Validation error") -> HTTPException:
    """
    Helper function to create validation error HTTPException.

    Args:
        detail (str): Error detail message

    Returns:
        HTTPException: FastAPI HTTPException instance with 422 status
    """
    return create_http_exception(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=detail
    )


def create_internal_error_exception(detail: str = "Internal server error") -> HTTPException:
    """
    Helper function to create internal server error HTTPException.

    Args:
        detail (str): Error detail message

    Returns:
        HTTPException: FastAPI HTTPException instance with 500 status
    """
    return create_http_exception(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=detail
    )


# Custom exception to HTTPException mapping
EXCEPTION_MAPPING = {
    TaskNotFoundException: lambda e: create_http_exception(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=e.message
    ),
    UserUnauthorizedException: lambda e: create_http_exception(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=e.message
    ),
    InvalidTokenException: lambda e: create_http_exception(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=e.message
    ),
    TaskValidationException: lambda e: create_http_exception(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=e.message
    ),
    DatabaseConnectionException: lambda e: create_http_exception(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=e.message
    ),
    DuplicateTaskException: lambda e: create_http_exception(
        status_code=status.HTTP_409_CONFLICT,
        detail=e.message
    )
}


def handle_custom_exception(exc: BaseCustomException) -> HTTPException:
    """
    Convert a custom exception to the appropriate HTTPException.

    Args:
        exc (BaseCustomException): The custom exception to convert

    Returns:
        HTTPException: The corresponding HTTPException
    """
    for exc_type, handler in EXCEPTION_MAPPING.items():
        if isinstance(exc, exc_type):
            return handler(exc)

    # Default to internal server error if no specific mapping found
    return create_internal_error_exception(str(exc))