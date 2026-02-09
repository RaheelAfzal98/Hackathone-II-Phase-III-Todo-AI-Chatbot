"""
MCP Tool: complete_task
This tool allows the AI agent to mark a task as completed.
"""

from typing import Dict, Any
from ..server import mcp_server
from sqlmodel import Session, select
from ...models.task import Task


@mcp_server.register_tool("complete_task")
async def complete_task(user_id: str, task_id: str) -> Dict[str, Any]:
    """
    Mark a task as completed for the specified user.

    Args:
        user_id: The ID of the user who owns the task
        task_id: The ID of the task to mark as completed

    Returns:
        Dictionary containing the updated task information
    """
    try:
        # Import database session here to avoid circular imports
        from sqlmodel import Session
        from src.database.connection import engine
        from src.services.task_service import TaskService
        from src.models.task import TaskUpdate

        # Validate inputs
        if not user_id or not task_id:
            return {
                "success": False,
                "error": "Both user_id and task_id are required"
            }

        # Create database session
        with Session(engine) as db_session:
            task_service = TaskService()

            # Update the task to mark as completed
            task_update = TaskUpdate(completed=True)
            updated_task = task_service.update_task(
                task_id=task_id,
                user_id=user_id,
                task_update=task_update,
                db=db_session
            )

            # Convert to dict for response
            task_dict = {
                "id": updated_task.id,
                "user_id": updated_task.user_id,
                "title": updated_task.title,
                "description": updated_task.description,
                "completed": updated_task.completed,
                "priority": updated_task.priority.value if hasattr(updated_task.priority, 'value') else updated_task.priority,
                "created_at": updated_task.created_at.isoformat() if hasattr(updated_task.created_at, 'isoformat') else str(updated_task.created_at),
                "updated_at": updated_task.updated_at.isoformat() if hasattr(updated_task.updated_at, 'isoformat') else str(updated_task.updated_at)
            }

            return {
                "success": True,
                "task": task_dict
            }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to complete task: {str(e)}"
        }


# For integration with the existing Phase II task system
def complete_task_with_db_session(user_id: str, task_id: str, db_session: Session = None) -> Dict[str, Any]:
    """
    Mark a task as completed for the specified user using database session.

    Args:
        user_id: The ID of the user who owns the task
        task_id: The ID of the task to mark as completed
        db_session: Database session to use for the operation

    Returns:
        Dictionary containing the updated task information
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

        # Update the task to mark as completed
        task.completed = True
        db_session.add(task)
        db_session.commit()
        db_session.refresh(task)

        # Convert to dictionary for response
        task_dict = {
            "id": task.id,
            "user_id": task.user_id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "priority": task.priority.value if hasattr(task.priority, 'value') else task.priority,
            "created_at": getattr(task, 'created_at', None),
            "updated_at": getattr(task, 'updated_at', None)
        }

        return {
            "success": True,
            "task": task_dict
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to complete task: {str(e)}"
        }