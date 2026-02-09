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

print("=== Testing AI Operations with Better Commands ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"test_ops_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"Ops Test {timestamp}"
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
        
        print("\n=== Adding tasks to work with ===")
        
        # Add some tasks first
        tasks_to_add = [
            "Add a task to buy milk",
            "Add a task to call doctor",
            "Add a task to finish project"
        ]
        
        for task_msg in tasks_to_add:
            msg = {"message": task_msg}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"  [OK] Added: {result.get('response', 'No response')}")
            else:
                print(f"  [ERROR] Failed to add task: {response.text}")
        
        # Wait a moment for tasks to be processed
        import time
        time.sleep(1)
        
        print("\n=== Listing tasks to get IDs ===")
        
        # List tasks to see what we have
        msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"  [OK] Tasks: {result.get('response', 'No response')}")
        else:
            print(f"  [ERROR] Failed to list tasks: {response.text}")
        
        print("\n=== Testing specific task operations (using task IDs) ===")
        
        # Now try operations with specific task IDs
        # First, get the actual tasks via the API to see their IDs
        tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        if tasks_response.status_code == 200:
            tasks = tasks_response.json()
            print(f"  Found {len(tasks)} tasks via API")
            
            if tasks:
                # Test complete task with specific ID
                first_task = tasks[0]
                task_id = first_task['id']
                task_title = first_task['title']
                
                print(f"\n  Testing complete task: '{task_title}' (ID: {task_id[:8]}...)")
                
                complete_msg = {"message": f"Complete task {task_id}"}
                response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=complete_msg, headers=headers)
                if response.status_code == 200:
                    result = response.json()
                    print(f"    [OK] Complete response: {result.get('response', 'No response')}")
                else:
                    print(f"    [ERROR] Complete failed: {response.text}")
                
                # Test delete task with specific ID
                if len(tasks) > 1:
                    second_task = tasks[1]
                    task_id_2 = second_task['id']
                    task_title_2 = second_task['title']
                    
                    print(f"\n  Testing delete task: '{task_title_2}' (ID: {task_id_2[:8]}...)")
                    
                    delete_msg = {"message": f"Delete task {task_id_2}"}
                    response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=delete_msg, headers=headers)
                    if response.status_code == 200:
                        result = response.json()
                        print(f"    [OK] Delete response: {result.get('response', 'No response')}")
                    else:
                        print(f"    [ERROR] Delete failed: {response.text}")
                
                # Test update task with specific ID
                third_task = tasks[-1]  # Last task
                task_id_3 = third_task['id']
                task_title_3 = third_task['title']
                
                print(f"\n  Testing update task: '{task_title_3}' (ID: {task_id_3[:8]}...)")
                
                update_msg = {"message": f"Update task {task_id_3} to have high priority"}
                response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=update_msg, headers=headers)
                if response.status_code == 200:
                    result = response.json()
                    print(f"    [OK] Update response: {result.get('response', 'No response')}")
                else:
                    print(f"    [ERROR] Update failed: {response.text}")
        
        print("\n=== Final task list ===")
        final_msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=final_msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"  [OK] Final tasks: {result.get('response', 'No response')}")
        else:
            print(f"  [ERROR] Failed to get final tasks: {response.text}")
        
        print("\n=== AI Operations Test Complete ===")
        
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        
except Exception as e:
    print(f"[ERROR] Error during test: {e}")
    import traceback
    traceback.print_exc()