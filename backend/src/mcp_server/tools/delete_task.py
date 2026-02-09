"""
MCP Tool: delete_task
This tool allows the AI agent to delete a task for a user.
"""

from typing import Dict, Any
from ..server import mcp_server
from sqlmodel import Session, select, delete
from ...models.task import Task


@mcp_server.register_tool("delete_task")
async def delete_task(user_id: str, task_id: str) -> Dict[str, Any]:
    """
    Delete a task for the specified user.

    Args:
        user_id: The ID of the user who owns the task
        task_id: The ID of the task to delete

    Returns:
        Dictionary containing the result of the operation
    """
    try:
        # Import database session here to avoid circular imports
        from sqlmodel import Session
        from src.database.connection import engine
        from src.services.task_service import TaskService

        # Validate inputs
        if not user_id or not task_id:
            return {
                "success": False,
                "error": "Both user_id and task_id are required"
            }

        # Create database session
        with Session(engine) as db_session:
            task_service = TaskService()

            # Delete the task
            success = task_service.delete_task(
                task_id=task_id,
                user_id=user_id,
                db=db_session
            )

            if success:
                return {
                    "success": True,
                    "message": f"Task {task_id} deleted successfully"
                }
            else:
                return {
                    "success": False,
                    "error": f"Task {task_id} not found or does not belong to user"
                }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to delete task: {str(e)}"
        }


# For integration with the existing Phase II task system
def delete_task_with_db_session(user_id: str, task_id: str, db_session: Session = None) -> Dict[str, Any]:
    """
    Delete a task for the specified user using database session.

    Args:
        user_id: The ID of the user who owns the task
        task_id: The ID of the task to delete
        db_session: Database session to use for the operation

    Returns:
        Dictionary containing the result of the operation
    """
    try:
        # Validate inputs
        if not user_id or not task_id:
            return {
                "success": False,
                "error": "Both user_id and task_id are required"
            }

        # Query the database for the specific task belonging to the user
        statement = select(Task).where(Task.user_id == user_id).where(Task.id == task_id)
        result = db_session.exec(statement)
        task = result.first()

        if not task:
            return {
                "success": False,
                "error": "Task not found or does not belong to user"
            }

        # Delete the task from the database
        db_session.delete(task)
        db_session.commit()

        return {
            "success": True,
            "message": f"Task {task_id} deleted successfully"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to delete task: {str(e)}"
        }