import os
import sys
import asyncio
import requests

# Set the correct environment variables before importing anything else
os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['NEON_DB_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['BETTER_AUTH_SECRET'] = 'pohwuyqoVn683bmFDoVzmtQq50Zn3bFV'
os.environ['SECRET_KEY'] = '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'
os.environ['OPENAI_API_KEY'] = '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'
os.environ['OPEN_ROUTER_API_KEY'] = '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'

print("Environment variables set correctly.")

# Test the MCP server communication directly
def test_mcp_communication():
    print("Testing MCP server communication...")
    
    # Test the add_task tool via HTTP request to MCP server
    mcp_url = "http://localhost:8001/execute"
    
    payload = {
        "name": "add_task",
        "arguments": {
            "user_id": "test_user_123",
            "title": "Test task from HTTP call",
            "description": "This is a test task created via HTTP call to MCP",
            "priority": "high"
        }
    }
    
    try:
        response = requests.post(mcp_url, json=payload, timeout=30)
        print(f"MCP server response status: {response.status_code}")
        print(f"MCP server response: {response.json()}")
    except Exception as e:
        print(f"Error calling MCP server: {e}")
        import traceback
        traceback.print_exc()

# Run the test
test_mcp_communication()