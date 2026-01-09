from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ....models.task import TaskCreate, TaskRead, TaskUpdate
from ....services.task_service import TaskService
from ....auth.dependencies import get_current_user_id, validate_user_id_in_path
from ....database.session import get_session


router = APIRouter()


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: str = Depends(validate_user_id_in_path),
    task_data: TaskCreate = None,
    db: Session = Depends(get_session)
):
    """
    Create a new task for the authenticated user.

    Args:
        user_id (str): User ID validated from JWT token and URL path
        task_data (TaskCreate): Task data to create
        db (Session): Database session

    Returns:
        TaskRead: Created task data
    """
    # Override user_id in task_data to ensure it matches the authenticated user
    task_data.user_id = user_id

    try:
        return TaskService.create_task(task_data, db)
    except HTTPException:
        # Re-raise HTTP exceptions from the service
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating task: {str(e)}"
        )


@router.get("/{task_id}", response_model=TaskRead)
def get_task(
    task_id: str,
    user_id: str = Depends(validate_user_id_in_path),
    db: Session = Depends(get_session)
):
    """
    Retrieve a specific task by ID for the authenticated user.

    Args:
        task_id (str): ID of the task to retrieve
        user_id (str): User ID validated from JWT token and URL path
        db (Session): Database session

    Returns:
        TaskRead: Retrieved task data
    """
    try:
        return TaskService.get_task(task_id, user_id, db)
    except HTTPException:
        # Re-raise HTTP exceptions from the service
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving task: {str(e)}"
        )


@router.get("/", response_model=List[TaskRead])
def get_tasks(
    user_id: str = Depends(validate_user_id_in_path),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_session)
):
    """
    Retrieve all tasks for the authenticated user.

    Args:
        user_id (str): User ID validated from JWT token and URL path
        skip (int): Number of records to skip (for pagination)
        limit (int): Maximum number of records to return (for pagination)
        db (Session): Database session

    Returns:
        List[TaskRead]: List of user's tasks
    """
    try:
        return TaskService.get_tasks(user_id, db, skip=skip, limit=limit)
    except HTTPException:
        # Re-raise HTTP exceptions from the service
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving tasks: {str(e)}"
        )


@router.put("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: str,
    task_update: TaskUpdate,
    user_id: str = Depends(validate_user_id_in_path),
    db: Session = Depends(get_session)
):
    """
    Update an existing task for the authenticated user.

    Args:
        task_id (str): ID of the task to update
        task_update (TaskUpdate): Updated task data
        user_id (str): User ID validated from JWT token and URL path
        db (Session): Database session

    Returns:
        TaskRead: Updated task data
    """
    try:
        return TaskService.update_task(task_id, user_id, task_update, db)
    except HTTPException:
        # Re-raise HTTP exceptions from the service
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating task: {str(e)}"
        )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: str,
    user_id: str = Depends(validate_user_id_in_path),
    db: Session = Depends(get_session)
):
    """
    Delete a specific task by ID for the authenticated user.

    Args:
        task_id (str): ID of the task to delete
        user_id (str): User ID validated from JWT token and URL path
        db (Session): Database session
    """
    try:
        success = TaskService.delete_task(task_id, user_id, db)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error deleting task"
            )
    except HTTPException:
        # Re-raise HTTP exceptions from the service
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting task: {str(e)}"
        )


@router.patch("/{task_id}/toggle", response_model=TaskRead)
def toggle_task_completion(
    task_id: str,
    user_id: str = Depends(validate_user_id_in_path),
    db: Session = Depends(get_session)
):
    """
    Toggle the completion status of a task for the authenticated user.

    Args:
        task_id (str): ID of the task to toggle
        user_id (str): User ID validated from JWT token and URL path
        db (Session): Database session

    Returns:
        TaskRead: Updated task data with toggled completion status
    """
    try:
        return TaskService.toggle_task_completion(task_id, user_id, db)
    except HTTPException:
        # Re-raise HTTP exceptions from the service
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error toggling task completion: {str(e)}"
        )