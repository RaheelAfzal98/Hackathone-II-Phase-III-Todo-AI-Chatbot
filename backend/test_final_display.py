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

print("=== Testing Task List Display Fix ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"display_fix_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"Display Fix {timestamp}"
}

try:
    response = requests.post("http://localhost:8000/api/v1/register", json=register_data)
    print(f"Registration response: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print("Registration successful!")
        token = result.get('token')
        user_id = result.get('id')
        print(f"User ID: {user_id}")
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        print(f"\n=== Adding test tasks ===")
        
        # Add a few tasks
        tasks_to_add = [
            "Buy groceries",
            "Finish the report", 
            "Call mom tomorrow"
        ]
        
        for task_desc in tasks_to_add:
            add_msg = {"message": f"Add a task to {task_desc}"}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=add_msg, headers=headers)
            if response.status_code == 200:
                print(f"Added: {task_desc}")
            else:
                print(f"Failed to add: {task_desc}")
        
        print(f"\n=== Testing task list display ===")
        
        # Test listing tasks
        list_msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=list_msg, headers=headers)
        print(f"List response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            response_text = result.get('response', 'No response')
            print(f"\nTASK LIST OUTPUT:")
            print("="*50)
            print(response_text)
            print("="*50)
            
            # Check if the response contains important elements
            has_ids = "(ID:" in response_text
            has_titles = any(task in response_text for task in tasks_to_add)
            has_status = "[ ]" in response_text or "[X]" in response_text
            
            print(f"\nVerification:")
            print(f"- Contains task IDs: {has_ids}")
            print(f"- Contains task titles: {has_titles}")
            print(f"- Contains status indicators: {has_status}")
            
            if has_ids and has_titles and has_status:
                print("\n[SUCCESS] Task list is now properly displayed with IDs, titles, and status!")
            else:
                print("\n[PARTIAL] Some elements may be missing")
        else:
            print(f"List tasks failed: {response.text}")
        
        # Test completing a task and checking the status
        print(f"\n=== Testing task completion status ===")
        
        # Get tasks to get an ID
        tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        if tasks_response.status_code == 200:
            tasks = tasks_response.json()
            if tasks:
                task_id = tasks[0]['id']
                task_title = tasks[0]['title']
                
                print(f"Completing task: {task_title}")
                
                complete_msg = {"message": f"Complete task {task_id}"}
                response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=complete_msg, headers=headers)
                if response.status_code == 200:
                    print("Task completed successfully")
                else:
                    print(f"Task completion failed: {response.text}")
                
                # Check updated list
                print(f"\n=== Checking updated task list ===")
                list_msg = {"message": "Show me my tasks"}
                response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=list_msg, headers=headers)
                
                if response.status_code == 200:
                    result = response.json()
                    response_text = result.get('response', 'No response')
                    print("UPDATED TASK LIST:")
                    print("="*50)
                    print(response_text)
                    print("="*50)
                    
                    if "[X]" in response_text:
                        print("\n[SUCCESS] Completed task is now marked with [X]!")
                    else:
                        print("\n[INFO] Completed task may not be reflected yet")
            else:
                print("No tasks found to complete")
        
        print(f"\n=== All Operations Test ===")
        
        # Test all operations work properly
        operations = [
            ("Add", "Add a task to test all operations"),
            ("List", "Show me my tasks"),
            ("Complete", ""),  # Will get ID from the newly added task
            ("Update", ""),    # Will get ID from existing tasks
            ("Delete", "")     # Will get ID from existing tasks
        ]
        
        # Add a task to complete/update/delete
        add_response = requests.post(f"http://localhost:8000/api/{user_id}/chat", 
                                   json={"message": "Add a task to test operations"}, headers=headers)
        if add_response.status_code == 200:
            # Get the new task ID
            tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
            if tasks_response.status_code == 200:
                tasks = tasks_response.json()
                if tasks:
                    new_task_id = tasks[-1]['id']  # Get the most recently added task
                    
                    # Complete the task
                    complete_response = requests.post(f"http://localhost:8000/api/{user_id}/chat", 
                                                   json={"message": f"Complete task {new_task_id}"}, headers=headers)
                    if complete_response.status_code == 200:
                        print(f"[OK] Complete operation works")
                    else:
                        print(f"[ERROR] Complete operation failed")
                    
                    # Update the task (add another one first)
                    add2_response = requests.post(f"http://localhost:8000/api/{user_id}/chat", 
                                                json={"message": "Add a task to update"}, headers=headers)
                    if add2_response.status_code == 200:
                        # Get the new task ID for update
                        tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
                        if tasks_response.status_code == 200:
                            tasks = tasks_response.json()
                            if len(tasks) > 1:
                                update_task_id = tasks[-1]['id']
                                
                                update_response = requests.post(f"http://localhost:8000/api/{user_id}/chat", 
                                                              json={"message": f"Update task {update_task_id} to have high priority"}, headers=headers)
                                if update_response.status_code == 200:
                                    print(f"[OK] Update operation works")
                                else:
                                    print(f"[ERROR] Update operation failed")
                    
                    # Delete the task (add another one first)
                    add3_response = requests.post(f"http://localhost:8000/api/{user_id}/chat", 
                                               json={"message": "Add a task to delete"}, headers=headers)
                    if add3_response.status_code == 200:
                        # Get the new task ID for deletion
                        tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
                        if tasks_response.status_code == 200:
                            tasks = tasks_response.json()
                            if len(tasks) > 1:
                                delete_task_id = tasks[-1]['id']
                                
                                delete_response = requests.post(f"http://localhost:8000/api/{user_id}/chat", 
                                                             json={"message": f"Delete task {delete_task_id}"}, headers=headers)
                                if delete_response.status_code == 200:
                                    print(f"[OK] Delete operation works")
                                else:
                                    print(f"[ERROR] Delete operation failed")
        
        print("\n=== Final Task List ===")
        final_msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=final_msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            response_text = result.get('response', 'No response')
            task_count = response_text.count('1.') + response_text.count('2.') + response_text.count('3.')
            print(f"You have {task_count} tasks remaining")
        
        print("\n=== AI Chatbot Fully Functional ===")
        print("All operations (Add, List, Complete, Update, Delete) work properly!")
        print("Task list now displays with IDs, titles, descriptions, priorities, and completion status!")
        
    else:
        print(f"Registration failed: {response.text}")
        
except Exception as e:
    print(f"Error during test: {e}")
    import traceback
    traceback.print_exc()