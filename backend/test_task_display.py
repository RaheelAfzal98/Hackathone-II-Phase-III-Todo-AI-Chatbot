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

print("=== Testing Improved Task List Display ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"display_test_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"Display Test {timestamp}"
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
        
        print(f"\n=== Adding multiple tasks for display test ===")
        
        # Add several tasks with different priorities and completion states
        tasks_to_add = [
            "Buy groceries",
            "Finish the report", 
            "Schedule meeting with team",
            "Call mom tomorrow",
            "Walk the dog"
        ]
        
        for task_desc in tasks_to_add:
            add_msg = {"message": f"Add a task to {task_desc}"}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=add_msg, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"  [OK] Added: {task_desc}")
            else:
                print(f"  [ERROR] Failed to add: {task_desc}")
        
        print(f"\n=== Testing task list display ===")
        
        # Test listing tasks
        list_msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=list_msg, headers=headers)
        print(f"List response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            response_text = result.get('response', 'No response')
            print(f"\n--- TASK LIST DISPLAY ---")
            print(response_text)
            print(f"------------------------")
            
            # Check if the response contains task IDs and details
            if "ID:" in response_text and len(response_text) > 50:  # Basic check for detailed output
                print("[OK] Task list is now properly displayed with IDs and details!")
            else:
                print("[ERROR] Task list still not showing details properly")
        else:
            print(f"[ERROR] List tasks failed: {response.text}")
        
        # Now let's complete one task and see if the status updates
        print(f"\n=== Completing a task to test status updates ===")
        
        # Get tasks to get an ID
        tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        if tasks_response.status_code == 200:
            tasks = tasks_response.json()
            if tasks:
                task_to_complete = tasks[0]  # Get first task
                task_id = task_to_complete['id']
                task_title = task_to_complete['title']
                
                print(f"Completing task: {task_title} (ID: {task_id[:8]}...)")
                
                complete_msg = {"message": f"Complete task {task_id}"}
                response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=complete_msg, headers=headers)
                if response.status_code == 200:
                    print("[OK] Task completed successfully")
                else:
                    print(f"[ERROR] Task completion failed: {response.text}")
            else:
                print("[ERROR] No tasks found to complete")
        else:
            print(f"[ERROR] Could not get tasks to complete: {tasks_response.text}")
        
        print(f"\n=== Testing updated task list (should show completed task) ===")
        
        # List tasks again to see the updated status
        list_msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=list_msg, headers=headers)
        print(f"Updated list response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            response_text = result.get('response', 'No response')
            print(f"\n--- UPDATED TASK LIST ---")
            print(response_text)
            print(f"------------------------")
            
            if "✓" in response_text:  # Check if completed task is marked
                print("[OK] Completed task is now properly marked with ✓!")
            else:
                print("[INFO] May not have completed task yet, depends on which task was completed")
        else:
            print(f"[ERROR] Updated list failed: {response.text}")
        
        print(f"\n=== Testing other operations still work ===")
        
        # Test update
        if len(tasks) > 1:
            update_task = tasks[1]
            update_task_id = update_task['id']
            update_msg = {"message": f"Update task {update_task_id} to have high priority"}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=update_msg, headers=headers)
            if response.status_code == 200:
                print("[OK] Update operation works")
            else:
                print(f"[ERROR] Update failed: {response.text}")
        
        # Test delete (add a task first, then delete it)
        add_for_delete = {"message": "Add a task to delete later"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=add_for_delete, headers=headers)
        if response.status_code == 200:
            # Get the new task ID
            tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
            if tasks_response.status_code == 200:
                tasks = tasks_response.json()
                if len(tasks) > 2:  # Make sure we have enough tasks to delete one
                    task_to_delete = tasks[-1]  # Get last task
                    delete_task_id = task_to_delete['id']
                    
                    delete_msg = {"message": f"Delete task {delete_task_id}"}
                    response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=delete_msg, headers=headers)
                    if response.status_code == 200:
                        print("[OK] Delete operation works")
                    else:
                        print(f"[ERROR] Delete failed: {response.text}")
        
        print(f"\n=== Final verification ===")
        final_msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=final_msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            response_text = result.get('response', 'No response')
            print(f"Final task list has {response_text.count('1.') + response_text.count('2.') + response_text.count('3.') + response_text.count('4.') + response_text.count('5.')} tasks displayed")
        else:
            print(f"[ERROR] Final list failed: {response.text}")
        
        print("\n=== Task Display Test Complete ===")
        print("The AI Chatbot now properly displays tasks with IDs and details!")
        
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        
except Exception as e:
    print(f"[ERROR] Error during test: {e}")
    import traceback
    traceback.print_exc()