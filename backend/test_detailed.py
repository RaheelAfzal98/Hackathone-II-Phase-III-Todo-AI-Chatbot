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

print("=== Detailed AI Operation Test ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"detailed_test_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"Detailed Test {timestamp}"
}

try:
    response = requests.post("http://localhost:8000/api/v1/register", json=register_data)
    print(f"Registration response: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print("[OK] Registration successful!")
        token = result.get('token')
        user_id = result.get('id')
        print(f"User ID: {user_id}")
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        print("\n=== Step 1: Add a task ===")
        add_msg = {"message": "Add a task to test completion"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=add_msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"[OK] Add task response: {result}")
        else:
            print(f"[ERROR] Add task failed: {response.text}")
        
        # Get the task ID from the database directly
        print("\n=== Step 2: Get task ID from database ===")
        tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        if tasks_response.status_code == 200:
            tasks = tasks_response.json()
            if tasks:
                task = tasks[0]  # Get the first task
                task_id = task['id']
                print(f"[OK] Found task ID: {task_id}")
                print(f"Task title: {task['title']}")
                print(f"Task completed: {task['completed']}")
            else:
                print("[ERROR] No tasks found")
                task_id = None
        else:
            print(f"[ERROR] Could not get tasks: {tasks_response.text}")
            task_id = None
        
        if task_id:
            print(f"\n=== Step 3: Try to complete task {task_id} ===")
            complete_msg = {"message": f"Complete task {task_id}"}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=complete_msg, headers=headers)
            print(f"Complete task response status: {response.status_code}")
            if response.status_code == 200:
                result = response.json()
                print(f"Complete task response: {json.dumps(result, indent=2)}")
            else:
                print(f"[ERROR] Complete task failed: {response.text}")
            
            print(f"\n=== Step 4: Check task status after completion ===")
            # Check the task status via API
            task_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks/{task_id}", headers=headers)
            if task_response.status_code == 200:
                task_detail = task_response.json()
                print(f"Task after completion: {json.dumps(task_detail, indent=2)}")
                print(f"Completed status: {task_detail.get('completed', 'Unknown')}")
            else:
                print(f"[ERROR] Could not get task details: {task_response.text}")
        
        print("\n=== Step 5: Test direct MCP server call ===")
        if task_id:
            # Test the MCP server directly
            mcp_payload = {
                "name": "complete_task",
                "arguments": {
                    "user_id": user_id,
                    "task_id": task_id
                }
            }
            mcp_response = requests.post("http://localhost:8001/execute", json=mcp_payload)
            print(f"MCP server response status: {mcp_response.status_code}")
            if mcp_response.status_code == 200:
                mcp_result = mcp_response.json()
                print(f"MCP server response: {json.dumps(mcp_result, indent=2)}")
            else:
                print(f"[ERROR] MCP server call failed: {mcp_response.text}")
        
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        
except Exception as e:
    print(f"[ERROR] Error during test: {e}")
    import traceback
    traceback.print_exc()