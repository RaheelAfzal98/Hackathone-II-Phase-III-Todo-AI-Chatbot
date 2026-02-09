import os
import sys
import asyncio

# Set the correct environment variables
os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['NEON_DB_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['BETTER_AUTH_SECRET'] = 'pohwuyqoVn683bmFDoVzmtQq50Zn3bFV'
os.environ['SECRET_KEY'] = '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'
os.environ['OPENAI_API_KEY'] = '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'
os.environ['OPEN_ROUTER_API_KEY'] = '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'

print("Testing the complete AI agent service flow...")

# Test the AI agent service's execute_tool_call method
def test_ai_agent_tool_execution():
    try:
        from src.services.ai_agent_service import AIAgentService
        
        # Create an AI agent service instance
        ai_service = AIAgentService(openrouter_api_key=os.getenv("OPEN_ROUTER_API_KEY"))
        
        # Test executing the add_task tool through the AI agent service
        result = ai_service.execute_tool_call(
            tool_name="add_task",
            tool_arguments={
                "user_id": "test_user_123",
                "title": "Test task from AI agent service",
                "description": "This task was created through the AI agent service",
                "priority": "medium"
            },
            user_id="test_user_123"
        )
        
        print("AI Agent Service Tool Execution Result:")
        print(result)
        
        # Test executing the list_tasks tool
        list_result = ai_service.execute_tool_call(
            tool_name="list_tasks",
            tool_arguments={
                "user_id": "test_user_123"
            },
            user_id="test_user_123"
        )
        
        print("\nList Tasks Result:")
        print(list_result)
        
    except Exception as e:
        print(f"Error in AI agent service test: {e}")
        import traceback
        traceback.print_exc()

# Run the test
test_ai_agent_tool_execution()