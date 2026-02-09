import asyncio
import sys
import os

# Add the backend directory to the path so we can import modules
sys.path.insert(0, r'E:\Hackathon II Phase III Todo AI Chatbot\backend')

# Set the environment variables to use SQLite
os.environ['DATABASE_URL'] = 'sqlite:///./todo_local.db'
os.environ['NEON_DB_URL'] = 'sqlite:///./todo_local.db'

async def test_list_tasks():
    try:
        from src.mcp_server.tools.list_tasks import list_tasks
        
        # Test with a user ID that might not exist
        result = await list_tasks(user_id="nonexistent_user")
        print("Result:", result)
        
        # Test with the actual user ID we created
        result2 = await list_tasks(user_id="ed4530c4-25f7-4e3d-8252-a9a5897baae0")
        print("Result with real user:", result2)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_list_tasks())