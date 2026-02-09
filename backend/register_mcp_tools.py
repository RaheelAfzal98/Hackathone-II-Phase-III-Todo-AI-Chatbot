"""
Script to register MCP tools with the server
"""
from src.mcp_server.server import mcp_server
# Import tools to register them - they register themselves when imported
from src.mcp_server.tools import add_task, list_tasks, complete_task, update_task, delete_task

def register_all_tools():
    """Register all MCP tools with the server"""
    print("Registering MCP tools...")

    # The tools are already registered when imported due to decorators in the files
    # Just importing them ensures they're registered with the server

    print(f"Registered tools: {list(mcp_server.tools.keys())}")
    return mcp_server

if __name__ == "__main__":
    register_all_tools()
    print("MCP tools registered successfully!")