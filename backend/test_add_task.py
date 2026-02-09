import os
import sys
import asyncio

# Set the correct environment variables before importing anything else
os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['NEON_DB_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['BETTER_AUTH_SECRET'] = 'pohwuyqoVn683bmFDoVzmtQq50Zn3bFV'
os.environ['SECRET_KEY'] = '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'
os.environ['OPENAI_API_KEY'] = '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'
os.environ['OPEN_ROUTER_API_KEY'] = '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'

print("Environment variables set correctly.")

# Test the add_task tool directly
async def test_add_task():
    try:
        from src.mcp_server.tools.add_task import add_task
        
        # Test adding a task
        result = await add_task(
            user_id="test_user_123",
            title="Test task from direct call",
            description="This is a test task created directly",
            priority="medium"
        )
        
        print("Add task result:", result)
        
        # Also test listing tasks
        from src.mcp_server.tools.list_tasks import list_tasks
        list_result = await list_tasks(user_id="test_user_123")
        print("List tasks result:", list_result)
        
    except Exception as e:
        print(f"Error in test: {e}")
        import traceback
        traceback.print_exc()

# Run the test
asyncio.run(test_add_task())