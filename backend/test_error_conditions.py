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

print("=== Testing Error Conditions ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"error_test_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"Error Test {timestamp}"
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
        
        print(f"\n=== Testing various completion commands ===")
        
        # Test cases that might cause the error
        test_cases = [
            # Case 1: Complete without specifying ID
            ("Complete the task to buy groceries", "Complete without ID"),
            # Case 2: Complete with non-existent ID
            ("Complete task 00000000-0000-0000-0000-000000000000", "Complete with fake ID"),
            # Case 3: Complete with malformed ID
            ("Complete task invalid-id", "Complete with invalid ID"),
            # Case 4: Proper complete with real ID (should work)
        ]
        
        # First, add a task to get a real ID
        add_msg = {"message": "Add a task to test completion with real ID"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=add_msg, headers=headers)
        if response.status_code == 200:
            # Get the real task ID
            tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
            if tasks_response.status_code == 200:
                tasks = tasks_response.json()
                if tasks:
                    real_task_id = tasks[0]['id']
                    test_cases.append((f"Complete task {real_task_id}", "Complete with real ID (should work)"))
                else:
                    print("[ERROR] No tasks found to get real ID")
            else:
                print(f"[ERROR] Could not get tasks: {tasks_response.text}")
        else:
            print(f"[ERROR] Could not add task: {response.text}")
        
        for command, description in test_cases:
            print(f"\n--- {description} ---")
            print(f"Command: {command}")
            
            chat_msg = {"message": command}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_msg, headers=headers)
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                response_text = result.get('response', 'No response')
                print(f"Response: {response_text}")
                
                # Check if this is the error we're looking for
                if "Tool execution failed" in response_text and "Failed to complete task:" in response_text:
                    print(f"[FOUND THE ERROR] This is the error condition: {response_text}")
                    
                    # Print more details
                    print(f"Tool calls: {result.get('tool_calls', [])}")
                    print(f"Tool responses: {result.get('tool_responses', [])}")
            else:
                print(f"[ERROR] Request failed: {response.text}")
        
        print(f"\n=== Testing other operations with edge cases ===")
        
        # Test update and delete with invalid IDs
        edge_case_commands = [
            (f"Update task 00000000-0000-0000-0000-000000000000 to have high priority", "Update with fake ID"),
            (f"Delete task 00000000-0000-0000-0000-000000000000", "Delete with fake ID"),
        ]
        
        for command, description in edge_case_commands:
            print(f"\n--- {description} ---")
            print(f"Command: {command}")
            
            chat_msg = {"message": command}
            response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=chat_msg, headers=headers)
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                response_text = result.get('response', 'No response')
                print(f"Response: {response_text}")
                
                if "Tool execution failed" in response_text:
                    print(f"[FOUND AN ERROR] {description}: {response_text}")
            else:
                print(f"[ERROR] Request failed: {response.text}")
        
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        
except Exception as e:
    print(f"[ERROR] Error during test: {e}")
    import traceback
    traceback.print_exc()