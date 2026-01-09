from typing import Any, Dict, Optional
import re
import logging
from datetime import datetime


def validate_user_id(user_id: str) -> bool:
    """
    Validate the format of a user ID.

    Args:
        user_id (str): User ID to validate

    Returns:
        bool: True if valid, False otherwise
    """
    # A valid user ID should be a non-empty string with reasonable length
    # In a real application, you might want to check for UUID format or other specific formats
    if not user_id or not isinstance(user_id, str) or len(user_id) == 0 or len(user_id) > 100:
        return False

    # Additional validation could be added here based on your specific requirements
    # For example, checking if it matches a UUID format:
    # uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    # return bool(re.match(uuid_pattern, user_id, re.IGNORECASE))

    return True


def validate_task_title(title: str) -> bool:
    """
    Validate the format of a task title.

    Args:
        title (str): Task title to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not title or not isinstance(title, str):
        return False

    # Check length constraints (as per model definition: 1-200 characters)
    if len(title) < 1 or len(title) > 200:
        return False

    # Check for potentially problematic content (optional additional validation)
    # For example, check for excessive whitespace or control characters
    if re.search(r'[\x00-\x1f\x7f]', title):
        return False

    return True


def validate_task_description(description: Optional[str]) -> bool:
    """
    Validate the format of a task description.

    Args:
        description (Optional[str]): Task description to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if description is None:
        return True  # Description is optional

    if not isinstance(description, str):
        return False

    # Check length constraints (as per model definition: max 1000 characters)
    if len(description) > 1000:
        return False

    # Check for potentially problematic content
    if re.search(r'[\x00-\x1f\x7f]', description):
        return False

    return True


def sanitize_input(text: str) -> str:
    """
    Sanitize user input by removing potentially harmful characters.

    Args:
        text (str): Input text to sanitize

    Returns:
        str: Sanitized text
    """
    if not text or not isinstance(text, str):
        return text

    # Remove control characters
    sanitized = re.sub(r'[\x00-\x1f\x7f]', '', text)

    # You could add more sanitization rules here as needed
    # For example, removing potentially dangerous HTML tags if the text is meant for display
    # sanitized = re.sub(r'<[^>]+>', '', sanitized)

    return sanitized


def format_response_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format response data for consistent API responses.

    Args:
        data (Dict[str, Any]): Raw response data

    Returns:
        Dict[str, Any]: Formatted response data
    """
    # Ensure datetime objects are properly formatted for JSON serialization
    for key, value in data.items():
        if isinstance(value, datetime):
            data[key] = value.isoformat()

    return data


def create_error_response(message: str, error_code: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a standardized error response.

    Args:
        message (str): Error message
        error_code (Optional[str]): Optional error code

    Returns:
        Dict[str, Any]: Standardized error response
    """
    response = {
        "success": False,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }

    if error_code:
        response["error_code"] = error_code

    return response


def create_success_response(data: Optional[Dict[str, Any]] = None, message: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a standardized success response.

    Args:
        data (Optional[Dict[str, Any]]): Optional response data
        message (Optional[str]): Optional success message

    Returns:
        Dict[str, Any]: Standardized success response
    """
    response = {
        "success": True,
        "timestamp": datetime.utcnow().isoformat()
    }

    if data is not None:
        response["data"] = data

    if message:
        response["message"] = message

    return response


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with the specified name and level.

    Args:
        name (str): Name of the logger
        level (int): Logging level

    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding multiple handlers if logger already has handlers
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def mask_sensitive_data(data: Dict[str, Any], fields_to_mask: list = ["token", "password", "secret"]) -> Dict[str, Any]:
    """
    Mask sensitive fields in data dictionary.

    Args:
        data (Dict[str, Any]): Data dictionary to mask
        fields_to_mask (list): List of field names to mask

    Returns:
        Dict[str, Any]: Data dictionary with sensitive fields masked
    """
    masked_data = data.copy()

    for key, value in masked_data.items():
        if key.lower() in [field.lower() for field in fields_to_mask]:
            masked_data[key] = "***MASKED***"
        elif isinstance(value, dict):
            masked_data[key] = mask_sensitive_data(value, fields_to_mask)

    return masked_data