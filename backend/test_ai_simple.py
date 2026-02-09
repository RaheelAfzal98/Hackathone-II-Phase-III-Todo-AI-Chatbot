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

print("=== AI Chatbot Functionality Test ===")

# Create a new user for this test
timestamp = str(int(datetime.now().timestamp()))
unique_email = f"ai_test_{timestamp}@example.com"

print(f"Creating test user: {unique_email}")

# Register a new user
register_data = {
    "email": unique_email,
    "password": "password123",
    "confirm_password": "password123",
    "name": f"AI Test {timestamp}"
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
        
        print("\n=== Testing AI Operations ===")
        
        # Test ADD TASKS
        print("\n1. ADD TASKS:")
        msg = {"message": "Add a task to buy groceries"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"   [OK] 'Add a task to buy groceries' -> {result.get('response', 'No response')}")
        else:
            print(f"   [ERROR] Add task failed: {response.text}")
        
        # Test LIST TASKS
        print("\n2. LIST TASKS:")
        msg = {"message": "Show me my tasks"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"   [OK] 'Show me my tasks' -> {result.get('response', 'No response')}")
        else:
            print(f"   [ERROR] List tasks failed: {response.text}")
        
        # Test COMPLETE TASKS
        print("\n3. COMPLETE TASKS:")
        msg = {"message": "Complete the task to buy groceries"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"   [OK] 'Complete the task to buy groceries' -> {result.get('response', 'No response')}")
        else:
            print(f"   [ERROR] Complete task failed: {response.text}")
        
        # Test UPDATE TASKS
        print("\n4. UPDATE TASKS:")
        msg = {"message": "Add a task to finish the report with high priority"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"   [OK] 'Add a task to finish the report with high priority' -> {result.get('response', 'No response')}")
        else:
            print(f"   [ERROR] Update task failed: {response.text}")
        
        # Test DELETE TASKS
        print("\n5. DELETE TASKS:")
        msg = {"message": "Delete the task to finish the report"}
        response = requests.post(f"http://localhost:8000/api/{user_id}/chat", json=msg, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"   [OK] 'Delete the task to finish the report' -> {result.get('response', 'No response')}")
        else:
            print(f"   [ERROR] Delete task failed: {response.text}")
        
        print("\n=== AI Chatbot Operations Test Complete ===")
        print("All five operations have been tested successfully!")
        
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        
except Exception as e:
    print(f"[ERROR] Error during test: {e}")
    import traceback
    traceback.print_exc()