"""
MCP Tool: list_tasks
This tool allows the AI agent to retrieve all tasks for a user.
"""

from typing import Dict, Any, List
from ..server import mcp_server
from sqlmodel import Session, select
from ...models.task import Task


@mcp_server.register_tool("list_tasks")
async def list_tasks(user_id: str, status: str = "all") -> Dict[str, Any]:
    """
    Retrieve tasks for the specified user.

    Args:
        user_id: The ID of the user whose tasks to retrieve
        status: Filter by status ('all', 'pending', 'completed') - defaults to 'all'

    Returns:
        Dictionary containing a list of tasks
    """
    try:
        # Import database session here to avoid circular imports
        from sqlmodel import Session
        from src.database.connection import engine
        from src.services.task_service import TaskService

        # Create database session
        with Session(engine) as db_session:
            task_service = TaskService()

            # Get all tasks for the user
            tasks = task_service.get_tasks(user_id=user_id, db=db_session)

            # Filter by status if specified
            if status == "pending":
                filtered_tasks = [task for task in tasks if not task.completed]
            elif status == "completed":
                filtered_tasks = [task for task in tasks if task.completed]
            else:  # all
                filtered_tasks = tasks

            # Convert to dict for response
            tasks_list = []
            for task in filtered_tasks:
                task_dict = {
                    "id": task.id,
                    "user_id": task.user_id,
                    "title": task.title,
                    "description": task.description,
                    "completed": task.completed,
                    "priority": task.priority.value if hasattr(task.priority, 'value') else task.priority,
                    "created_at": task.created_at.isoformat() if hasattr(task.created_at, 'isoformat') else str(task.created_at),
                    "updated_at": task.updated_at.isoformat() if hasattr(task.updated_at, 'isoformat') else str(task.updated_at)
                }
                tasks_list.append(task_dict)

            return {
                "success": True,
                "tasks": tasks_list
            }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to list tasks: {str(e)}"
        }


# For integration with the existing Phase II task system
def list_tasks_with_db_session(user_id: str, db_session: Session = None) -> Dict[str, Any]:
    """
    Retrieve all tasks for the specified user using database session.

    Args:
        user_id: The ID of the user whose tasks to retrieve
        db_session: Database session to use for the operation

    Returns:
        Dictionary containing a list of tasks
    """
    try:
        # Query the database for tasks belonging to the user
        statement = select(Task).where(Task.user_id == user_id)
        results = db_session.exec(statement)
        tasks = results.all()

        # Convert tasks to dictionaries
        tasks_list = []
        for task in tasks:
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
            tasks_list.append(task_dict)

        return {
            "success": True,
            "tasks": tasks_list
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to list tasks: {str(e)}"
        }