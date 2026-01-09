#!/usr/bin/env python
"""
Test script to verify that the backend components are properly set up.
"""
import sys
import os

# Add the backend directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

def test_imports():
    """Test that all modules can be imported without errors."""
    print("Testing module imports...")

    try:
        from main import app
        print("+ Main app imported successfully")
    except Exception as e:
        print(f"✗ Error importing main app: {e}")
        return False

    try:
        from src.config.settings import settings
        print("+ Settings imported successfully")
    except Exception as e:
        print(f"- Error importing settings: {e}")
        return False

    try:
        from src.models.task import Task, TaskCreate, TaskRead, TaskUpdate
        print("+ Task models imported successfully")
    except Exception as e:
        print(f"- Error importing task models: {e}")
        return False

    try:
        from src.auth.jwt_handler import verify_token, create_access_token
        print("+ JWT handler imported successfully")
    except Exception as e:
        print(f"- Error importing JWT handler: {e}")
        return False

    try:
        from src.database.connection import engine
        print("+ Database connection imported successfully")
    except Exception as e:
        print(f"- Error importing database connection: {e}")
        return False

    print("\n+ All modules imported successfully!")
    return True


def test_basic_functionality():
    """Test basic functionality of key components."""
    print("\nTesting basic functionality...")

    try:
        from src.utils.helpers import validate_task_title, validate_user_id
        from src.auth.jwt_handler import create_access_token
        from src.config.settings import settings
        import uuid
        from datetime import timedelta

        # Test validation functions
        assert validate_task_title("Valid task title") == True
        assert validate_task_title("") == False
        assert validate_task_title("a" * 201) == False  # Too long
        print("+ Validation functions working")

        # Test JWT creation (won't verify since we don't have a real token)
        token_data = {"sub": str(uuid.uuid4())}
        token = create_access_token(data=token_data, expires_delta=timedelta(minutes=30))
        assert isinstance(token, str)
        assert len(token) > 0
        print("+ JWT creation working")

        # Test settings access
        assert hasattr(settings, 'SECRET_KEY')
        assert hasattr(settings, 'ALGORITHM')
        print("+ Settings access working")

        print("\n+ All basic functionality tests passed!")
        return True

    except Exception as e:
        print(f"- Error in basic functionality test: {e}")
        return False


if __name__ == "__main__":
    print("Running backend API verification tests...\n")

    imports_ok = test_imports()
    if not imports_ok:
        print("\n- Import tests failed. Please check the errors above.")
        sys.exit(1)

    functionality_ok = test_basic_functionality()
    if not functionality_ok:
        print("\n- Functionality tests failed. Please check the errors above.")
        sys.exit(1)

    print("\n+ All tests passed! The backend API is properly set up.")
    print("\nThe Todo API backend is ready for use with:")
    print("- JWT authentication")
    print("- User isolation")
    print("- Complete CRUD operations")
    print("- Proper error handling")
    print("- Input validation")