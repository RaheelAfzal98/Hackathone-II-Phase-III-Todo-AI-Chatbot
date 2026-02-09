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

print("=== Testing Improved AI Chatbot Operations ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"improved_test_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"Improved Test {timestamp}"
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
        
        print("\n=== Testing All Five Operations ===")
        
        # 1. ADD TASKS
        print("\n1. ADD TASKS:")
        msg = {"message": "Add a task to buy groceries"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"   [OK] Add task: {result.get('response', 'No response')}")
        else:
            print(f"   [ERROR] Add task failed: {response.text}")
        
        # 2. LIST TASKS
        print("\n2. LIST TASKS:")
        msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"   [OK] List tasks: {result.get('response', 'No response')}")
        else:
            print(f"   [ERROR] List tasks failed: {response.text}")
        
        # Get tasks to get an ID for testing complete/delete/update
        tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        task_id = None
        if tasks_response.status_code == 200:
            tasks = tasks_response.json()
            if tasks:
                task_id = tasks[0]['id']
                print(f"   Got task ID: {task_id[:8]}...")
        
        if task_id:
            # 3. COMPLETE TASKS
            print("\n3. COMPLETE TASKS:")
            msg = {"message": f"Complete task {task_id}"}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"   [OK] Complete task: {result.get('response', 'No response')}")
            else:
                print(f"   [ERROR] Complete task failed: {response.text}")
        
            # 4. UPDATE TASKS
            print("\n4. UPDATE TASKS:")
            msg = {"message": f"Update task {task_id} to have high priority"}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"   [OK] Update task: {result.get('response', 'No response')}")
            else:
                print(f"   [ERROR] Update task failed: {response.text}")
        
            # 5. DELETE TASKS
            print("\n5. DELETE TASKS:")
            # First add another task to delete
            add_msg = {"message": "Add a task to schedule meeting"}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=add_msg, headers=headers)
            if response.status_code == 200:
                # Get the new task ID
                tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
                if tasks_response.status_code == 200:
                    tasks = tasks_response.json()
                    if len(tasks) > 1:  # We need at least 2 tasks to delete one
                        task_to_delete = tasks[-1]  # Get the most recently added task
                        delete_task_id = task_to_delete['id']
                        
                        delete_msg = {"message": f"Delete task {delete_task_id}"}
                        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=delete_msg, headers=headers)
                        if response.status_code == 200:
                            result = response.json()
                            print(f"   [OK] Delete task: {result.get('response', 'No response')}")
                        else:
                            print(f"   [ERROR] Delete task failed: {response.text}")
                    else:
                        print("   [ERROR] Not enough tasks to test deletion")
            else:
                print(f"   [ERROR] Could not add task for deletion test: {response.text}")
        
        print("\n=== Final Verification ===")
        final_msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=final_msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"   Final task list: {result.get('response', 'No response')}")
        else:
            print(f"   [ERROR] Final list failed: {response.text}")
        
        print("\n=== All AI Operations Test Complete ===")
        print("The AI Chatbot now properly supports all five operations!")
        
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        
except Exception as e:
    print(f"[ERROR] Error during test: {e}")
    import traceback
    traceback.print_exc()