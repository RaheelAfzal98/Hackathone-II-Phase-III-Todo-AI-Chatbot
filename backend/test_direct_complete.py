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

print("=== Testing Complete Task Tool Directly ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"direct_test_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"Direct Test {timestamp}"
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
        
        print("\n=== Adding a test task ===")
        # Add a task first
        add_msg = {"message": "Add a task to test completion directly"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=add_msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"[OK] Task added: {result.get('response', 'No response')}")
        else:
            print(f"[ERROR] Failed to add task: {response.text}")
        
        # Get the task ID
        tasks_response = requests.get(f"http://localhost:8000/api/v1/users/{user_id}/tasks", headers=headers)
        if tasks_response.status_code == 200:
            tasks = tasks_response.json()
            if tasks:
                task_id = tasks[0]['id']
                print(f"[OK] Got task ID: {task_id}")
                
                print(f"\n=== Testing complete_task tool via MCP server directly ===")
                # Test the complete_task tool directly via MCP server
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
                    print(f"MCP server result: {json.dumps(mcp_result, indent=2)}")
                    
                    if mcp_result.get('success') == True:
                        print("[OK] Direct MCP call succeeded!")
                    else:
                        print(f"[ERROR] MCP call failed: {mcp_result.get('error', 'Unknown error')}")
                else:
                    print(f"[ERROR] MCP server call failed: {mcp_response.text}")
                
                print(f"\n=== Testing via AI chat endpoint ===")
                # Now test via the AI chat endpoint
                complete_msg = {"message": f"Complete task {task_id}"}
                response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=complete_msg, headers=headers)
                print(f"AI chat response status: {response.status_code}")
                
                if response.status_code == 200:
                    result = response.json()
                    print(f"AI chat result: {json.dumps(result, indent=2)}")
                    
                    if "error" in result.get('response', '').lower():
                        print("[ERROR] AI chat reported an error!")
                    else:
                        print("[OK] AI chat succeeded!")
                else:
                    print(f"[ERROR] AI chat failed: {response.text}")
            else:
                print("[ERROR] No tasks found")
        else:
            print(f"[ERROR] Could not get tasks: {tasks_response.text}")
        
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        
except Exception as e:
    print(f"[ERROR] Error during test: {e}")
    import traceback
    traceback.print_exc()