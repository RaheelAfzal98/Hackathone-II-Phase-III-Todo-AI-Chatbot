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

print("Testing with correct API endpoints...")

# Login with the existing test user
login_data = {
    "email": "user_1770658762@example.com",  # Use the email from the previous test
    "password": "password123"
}

try:
    response = requests.post("http://localhost:8000/api/v1/login", json=login_data)
    print(f"Login response status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Login successful!")
        print(f"User ID: {result.get('id')}")
        
        # Store the token for later use
        token = result.get('token')
        user_id = result.get('id')
        
        # Test adding a task with the correct endpoint
        print(f"\nTesting task creation with correct endpoint (User ID: {user_id})...")
        
        task_data = {
            "title": "Test task via correct API",
            "description": "This is a test task created via the correct API endpoint",
            "priority": "medium"
        }
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # Use the correct endpoint: /api/v1/users/{user_id}/tasks
        task_response = requests.post(f"http://localhost:8000/api/v1/users/{user_id}/tasks", json=task_data, headers=headers)
        print(f"Task creation response status: {task_response.status_code}")
        
        if task_response.status_code == 201:  # 201 for created
            task_result = task_response.json()
            print(f"Task created successfully: {task_result.get('id')}")
            task_id = task_result.get('id')
        else:
            print(f"Task creation failed: {task_response.text}")
            # Try to register a new user just in case
            timestamp = str(int(datetime.now().timestamp()))
            unique_email = f"user_{timestamp}@example.com"
            
            register_data = {
                "email": unique_email,
                "password": "password123",
                "confirm_password": "password123",
                "name": f"Test User {timestamp}"
            }
            
            reg_response = requests.post("http://localhost:8000/api/v1/register", json=register_data)
            if reg_response.status_code == 200:
                reg_result = reg_response.json()
                token = reg_result.get('token')
                user_id = reg_result.get('id')
                
                print(f"Using newly registered user: {user_id}")
                
                # Retry task creation
                task_response = requests.post(f"http://localhost:8000/api/v1/users/{user_id}/tasks", json=task_data, headers=headers)
                print(f"Retry task creation response status: {task_response.status_code}")
                
                if task_response.status_code == 201:
                    task_result = task_response.json()
                    print(f"Task created successfully: {task_result.get('id')}")
                    task_id = task_result.get('id')
                else:
                    print(f"Retry task creation failed: {task_response.text}")
                    task_id = None
            else:
                print(f"Failed to register new user: {reg_response.text}")
                task_id = None
        
        if task_id:
            # Test getting tasks
            print("\nTesting task retrieval...")
            get_tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
            print(f"Get tasks response status: {get_tasks_response.status_code}")
            
            if get_tasks_response.status_code == 200:
                tasks_result = get_tasks_response.json()
                print(f"Retrieved {len(tasks_result)} tasks")
                for task in tasks_result:
                    print(f"  - {task.get('title')} (ID: {task.get('id')[:8]}...)")
            
            # Test getting specific task
            print(f"\nTesting specific task retrieval (Task ID: {task_id[:8]}...)...")
            get_task_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks/{task_id}", headers=headers)
            print(f"Get specific task response status: {get_task_response.status_code}")
            
            if get_task_response.status_code == 200:
                task_detail = get_task_response.json()
                print(f"Retrieved task: {task_detail.get('title')}")
            
            # Test toggling task completion
            print(f"\nTesting task toggle (Task ID: {task_id[:8]}...)...")
            toggle_response = requests.patch(f"http://localhost:8000/api/v1/users/{user_id}/tasks/{task_id}/toggle", headers=headers)
            print(f"Toggle task response status: {toggle_response.status_code}")
            
            if toggle_response.status_code == 200:
                toggle_result = toggle_response.json()
                print(f"Task toggled. Completed: {toggle_result.get('completed')}")
        
        # Test the chat endpoint as well
        print(f"\nTesting chat endpoint with user (ID: {user_id})...")
        chat_data = {
            "message": "Add a task to walk the dog"
        }
        
        chat_response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_data, headers=headers)
        print(f"Chat response status: {chat_response.status_code}")
        
        if chat_response.status_code == 200:
            chat_result = chat_response.json()
            print(f"Chat successful: {chat_result.get('response', 'No response text')}")
            print(f"Tool calls: {len(chat_result.get('tool_calls', []))}")
        else:
            print(f"Chat failed: {chat_response.text}")
        
    else:
        print(f"Login failed: {response.text}")
        
except Exception as e:
    print(f"Error during test: {e}")
    import traceback
    traceback.print_exc()