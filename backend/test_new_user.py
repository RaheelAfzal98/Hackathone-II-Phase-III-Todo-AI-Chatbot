import os
import sys
import requests
import json
from datetime import datetime

# Set the correct environment variables
os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['NEON_DB_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['BETTER_AUTH_SECRET'] = 'pohwuyqoVn683bmFDoVzmtQq50Zn3bFV'
os.environ['SECRET_KEY'] = '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'
os.environ['OPENAI_API_KEY'] = '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'
os.environ['OPEN_ROUTER_API_KEY'] = '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'

# Create a unique email address
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"user_{timestamp}@example.com"

print(f"Creating a new user with unique email: {unique_email}")

# Register a new user with unique email
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"Test User {timestamp}"
}

try:
    response = requests.post("http://localhost:8000/api/v1/register", json=register_data)
    print(f"Registration response status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Registration successful!")
        print(f"User ID: {result.get('id')}")
        print(f"User Email: {result.get('email')}")
        print(f"Token: {result.get('token')[:20]}...")  # Show first 20 chars of token
        
        # Store the token for later use
        token = result.get('token')
        user_id = result.get('id')
        
        # Test adding a task with the authenticated user
        print(f"\nTesting task creation with authenticated user (ID: {user_id})...")
        
        task_data = {
            "title": "Test task via API",
            "description": "This is a test task created via the API",
            "priority": "medium"
        }
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # Note: The API expects user_id in the URL path
        task_response = requests.post(f"http://localhost:8000/api/v1/{user_id}", json=task_data, headers=headers)
        print(f"Task creation response status: {task_response.status_code}")
        
        if task_response.status_code == 200:
            task_result = task_response.json()
            print(f"Task created successfully: {task_result.get('id')}")
        else:
            print(f"Task creation failed: {task_response.text}")
            
        # Test getting tasks
        print("\nTesting task retrieval...")
        get_tasks_response = requests.get(f"http://localhost:8000/api/v1/{user_id}", headers=headers)
        print(f"Get tasks response status: {get_tasks_response.status_code}")
        
        if get_tasks_response.status_code == 200:
            tasks_result = get_tasks_response.json()
            print(f"Retrieved {len(tasks_result)} tasks")
            for task in tasks_result:
                print(f"  - {task.get('title')} (ID: {task.get('id')[:8]}...)")
        else:
            print(f"Get tasks failed: {get_tasks_response.text}")
        
        # Test the chat endpoint with the authenticated user
        print(f"\nTesting chat endpoint with user (ID: {user_id})...")
        chat_data = {
            "message": "Add a task to buy groceries"
        }
        
        chat_response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_data, headers=headers)
        print(f"Chat response status: {chat_response.status_code}")
        
        if chat_response.status_code == 200:
            chat_result = chat_response.json()
            print(f"Chat successful: {chat_result.get('response', 'No response text')}")
        else:
            print(f"Chat failed: {chat_response.text}")
        
    else:
        print(f"Registration failed: {response.text}")
        
except Exception as e:
    print(f"Error during test: {e}")
    import traceback
    traceback.print_exc()