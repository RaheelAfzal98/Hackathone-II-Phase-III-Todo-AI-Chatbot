import os
import sys
import requests
import json
import time
from datetime import datetime

# Set the correct environment variables
os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['NEON_DB_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['BETTER_AUTH_SECRET'] = 'pohwuyqoVn683bmFDoVzmtQq50Zn3bFV'
os.environ['SECRET_KEY'] = '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'
os.environ['OPENAI_API_KEY'] = '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'
os.environ['OPEN_ROUTER_API_KEY'] = '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'

print("=== AI Chatbot Functionality Test ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"ai_test_user_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"AI Test User {timestamp}"
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
        
        print("\n=== Testing AI Chatbot Commands ===")
        
        # 1. ADD TASKS
        print("\n1. Testing ADD TASKS command...")
        add_task_messages = [
            "Add a task to buy groceries",
            "Create a task to finish the report",
            "Add task to call mom tomorrow"
        ]
        
        for msg in add_task_messages:
            chat_data = {"message": msg}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_data, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"  [OK] '{msg}' -> {result.get('response', 'No response')}")
            else:
                print(f"  [ERROR] '{msg}' -> Failed: {response.text}")
        
        # Wait a moment for tasks to be processed
        time.sleep(1)
        
        # 2. LIST TASKS
        print("\n2. Testing LIST TASKS command...")
        list_messages = [
            "Show me my tasks",
            "What tasks do I have?",
            "List all my tasks"
        ]
        
        for msg in list_messages:
            chat_data = {"message": msg}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_data, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"  [OK] '{msg}' -> {result.get('response', 'No response')}")
            else:
                print(f"  [ERROR] '{msg}' -> Failed: {response.text}")
        
        # Wait a moment
        time.sleep(1)
        
        # 3. COMPLETE TASKS
        print("\n3. Testing COMPLETE TASKS command...")
        # First, let's get the tasks to know their IDs
        get_tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        if get_tasks_response.status_code == 200:
            tasks = get_tasks_response.json()
            if tasks:
                task_to_complete = tasks[0]  # Take the first task
                task_id = task_to_complete['id']
                task_title = task_to_complete['title']
                
                complete_messages = [
                    f"Mark task {task_id} as complete",
                    f"Complete the task '{task_title}'",
                    f"Finish the task with ID {task_id}"
                ]
                
                for msg in complete_messages:
                    chat_data = {"message": msg}
                    response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_data, headers=headers)
                    if response.status_code == 200:
                        result = response.json()
                        print(f"  [OK] '{msg}' -> {result.get('response', 'No response')}")
                    else:
                        print(f"  [ERROR] '{msg}' -> Failed: {response.text}")
            else:
                print("  No tasks found to complete")
        else:
            print(f"  Could not retrieve tasks: {get_tasks_response.text}")
        
        # Wait a moment
        time.sleep(1)
        
        # 4. UPDATE TASKS
        print("\n4. Testing UPDATE TASKS command...")
        # Get tasks again to pick one to update
        get_tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        if get_tasks_response.status_code == 200:
            tasks = get_tasks_response.json()
            if tasks:
                task_to_update = tasks[0]  # Take the first task
                task_id = task_to_update['id']
                task_title = task_to_update['title']
                
                update_messages = [
                    f"Update task {task_id} to have high priority",
                    f"Change the description of '{task_title}' to 'Updated description'",
                    f"Modify task {task_id} to have medium priority"
                ]
                
                for msg in update_messages:
                    chat_data = {"message": msg}
                    response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_data, headers=headers)
                    if response.status_code == 200:
                        result = response.json()
                        print(f"  [OK] '{msg}' -> {result.get('response', 'No response')}")
                    else:
                        print(f"  [ERROR] '{msg}' -> Failed: {response.text}")
            else:
                print("  No tasks found to update")
        else:
            print(f"  Could not retrieve tasks: {get_tasks_response.text}")
        
        # Wait a moment
        time.sleep(1)
        
        # 5. DELETE TASKS
        print("\n5. Testing DELETE TASKS command...")
        # Get tasks again to pick one to delete
        get_tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        if get_tasks_response.status_code == 200:
            tasks = get_tasks_response.json()
            if len(tasks) >= 2:  # Need at least 2 tasks to safely delete one
                task_to_delete = tasks[-1]  # Take the last task
                task_id = task_to_delete['id']
                task_title = task_to_delete['title']
                
                delete_messages = [
                    f"Delete task {task_id}",
                    f"Remove the task '{task_title}'",
                    f"Delete the task with ID {task_id}"
                ]
                
                for msg in delete_messages:
                    chat_data = {"message": msg}
                    response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_data, headers=headers)
                    if response.status_code == 200:
                        result = response.json()
                        print(f"  [OK] '{msg}' -> {result.get('response', 'No response')}")
                    else:
                        print(f"  [ERROR] '{msg}' -> Failed: {response.text}")
            else:
                print("  Not enough tasks to test deletion (need at least 2)")
        else:
            print(f"  Could not retrieve tasks: {get_tasks_response.text}")
        
        # Final verification: list all tasks to see the current state
        print("\n6. Final verification - listing all remaining tasks...")
        final_msg = {"message": "Show me all my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=final_msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"  Final task list: {result.get('response', 'No response')}")
        else:
            print(f"  Failed to get final task list: {response.text}")
        
        print("\n=== AI Chatbot Functionality Test Complete ===")
        print("All operations (Add, List, Complete, Update, Delete) have been tested with AI commands.")
        
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        
except Exception as e:
    print(f"[ERROR] Error during test: {e}")
    import traceback
    traceback.print_exc()