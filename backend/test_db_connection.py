import asyncio
import sys
import os

# Add the backend directory to the path so we can import modules
sys.path.insert(0, r'E:\Hackathon II Phase III Todo AI Chatbot\backend')

# Set the environment variables to use SQLite
os.environ['DATABASE_URL'] = 'sqlite:///./todo_local.db'
os.environ['NEON_DB_URL'] = 'sqlite:///./todo_local.db'

async def test_database_connection():
    try:
        # Test if we can import and access the database engine
        from src.database.connection import engine
        print("Engine imported successfully")
        print(f"Engine URL: {engine.url}")
        
        # Test the ping function
        from src.database.connection import ping_database
        is_connected = ping_database()
        print(f"Database ping result: {is_connected}")
        
        # Test the list_tasks tool again with more detailed error reporting
        from src.mcp_server.tools.list_tasks import list_tasks
        
        # Test with the actual user ID we created
        result = await list_tasks(user_id="ed4530c4-25f7-4e3d-8252-a9a5897baae0")
        print("Direct tool call result:", result)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_database_connection())