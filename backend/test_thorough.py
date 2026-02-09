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

print("=== Testing All Task Operations Thoroughly ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"thorough_test_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"Thorough Test {timestamp}"
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
        
        # Add multiple tasks for testing
        tasks_to_add = [
            "Add a task to test completion",
            "Add a task to test update", 
            "Add a task to test deletion"
        ]
        
        print(f"\n=== Adding test tasks ===")
        for task_desc in tasks_to_add:
            add_msg = {"message": task_desc}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=add_msg, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"  [OK] Added: {result.get('response', 'No response')}")
            else:
                print(f"  [ERROR] Failed to add: {response.text}")
        
        # Get all tasks
        tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        if tasks_response.status_code == 200:
            tasks = tasks_response.json()
            print(f"\n[OK] Retrieved {len(tasks)} tasks")
            
            if len(tasks) >= 3:
                # Get specific task IDs for each operation
                complete_task = tasks[0]
                update_task = tasks[1] 
                delete_task = tasks[2]
                
                print(f"Complete task ID: {complete_task['id'][:8]}... - '{complete_task['title']}'")
                print(f"Update task ID: {update_task['id'][:8]}... - '{update_task['title']}'")
                print(f"Delete task ID: {delete_task['id'][:8]}... - '{delete_task['title']}'")
                
                # Test each operation individually
                operations = [
                    ("Complete", f"Complete task {complete_task['id']}"),
                    ("Update", f"Update task {update_task['id']} to have high priority"),
                    ("Delete", f"Delete task {delete_task['id']}")
                ]
                
                for op_name, command in operations:
                    print(f"\n=== Testing {op_name} Operation ===")
                    print(f"Command: {command}")
                    
                    chat_msg = {"message": command}
                    response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_msg, headers=headers)
                    print(f"Response status: {response.status_code}")
                    
                    if response.status_code == 200:
                        result = response.json()
                        print(f"Response: {result.get('response', 'No response')}")
                        
                        # Check if there are tool calls and results
                        if result.get('tool_calls'):
                            print(f"Tool calls made: {len(result['tool_calls'])}")
                            for i, call in enumerate(result['tool_calls']):
                                print(f"  Tool call {i+1}: {call['name']} with args {call['arguments']}")
                        
                        if 'error' in result.get('response', '').lower():
                            print(f"[ERROR] Operation reported an error in response: {result['response']}")
                        else:
                            print(f"[OK] {op_name} operation completed successfully")
                    else:
                        print(f"[ERROR] {op_name} operation failed: {response.text}")
                
                # Final check - list all remaining tasks
                print(f"\n=== Final Task List ===")
                list_msg = {"message": "Show me my tasks"}
                response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=list_msg, headers=headers)
                if response.status_code == 200:
                    result = response.json()
                    print(f"Final response: {result.get('response', 'No response')}")
                else:
                    print(f"[ERROR] Final list failed: {response.text}")
            else:
                print(f"[ERROR] Not enough tasks created ({len(tasks)})")
        else:
            print(f"[ERROR] Could not retrieve tasks: {tasks_response.text}")
        
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        
except Exception as e:
    print(f"[ERROR] Error during test: {e}")
    import traceback
    traceback.print_exc()