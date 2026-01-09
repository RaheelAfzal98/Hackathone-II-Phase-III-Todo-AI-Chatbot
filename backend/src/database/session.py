from contextlib import contextmanager
from sqlalchemy.orm import Session, sessionmaker
from typing import Generator
from .connection import engine


# Create a session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Generator[Session, None, None]:
    """
    Dependency to get database session for FastAPI endpoints.

    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_session():
    """
    Context manager to get database session for use outside of FastAPI endpoints.

    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_session_sync() -> Session:
    """
    Synchronous function to get database session.

    Returns:
        Session: SQLAlchemy database session (remember to close it manually)
    """
    return SessionLocal()


def close_session(db: Session):
    """
    Close the database session.

    Args:
        db (Session): SQLAlchemy database session to close
    """
    db.close()


# Convenience function to run database operations with automatic session management
def run_db_operation(operation_func, *args, **kwargs):
    """
    Run a database operation with automatic session management.

    Args:
        operation_func: Function to run with database session
        *args: Arguments to pass to the operation function
        **kwargs: Keyword arguments to pass to the operation function

    Returns:
        Result of the operation function
    """
    with get_db_session() as db:
        kwargs['db'] = db
        return operation_func(*args, **kwargs)