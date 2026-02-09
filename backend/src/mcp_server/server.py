"""
MCP Server for AI Chatbot Integration
This module implements the Model Context Protocol server that exposes
task operations as tools for the AI agent.
"""

import asyncio
import json
from typing import Dict, Any, List
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware


# Global configuration
MCP_SERVER_URL = "http://localhost:8001"  # Default URL for the MCP server


class ToolCall(BaseModel):
    name: str
    arguments: Dict[str, Any]


class ToolResult(BaseModel):
    success: bool
    result: Any = None
    error: str = None


class MCPServer:
    def __init__(self):
        self.app = FastAPI(title="MCP Server for AI Chatbot", version="1.0.0")
        self.tools = {}

        # Add CORS middleware
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self._setup_routes()

    def _setup_routes(self):
        @self.app.get("/")
        async def root():
            return {"message": "MCP Server for AI Chatbot Integration"}

        @self.app.post("/execute")
        async def execute_tool(call: ToolCall):
            """Execute a registered tool with the provided arguments."""
            if call.name not in self.tools:
                raise HTTPException(status_code=404, detail=f"Tool {call.name} not found")

            try:
                # Execute the tool function
                result = await self.tools[call.name](**call.arguments)
                return ToolResult(success=True, result=result)
            except Exception as e:
                return ToolResult(success=False, error=str(e))

        @self.app.get("/tools")
        async def list_tools():
            """Return a list of available tools."""
            return {"tools": list(self.tools.keys())}

    def register_tool(self, name: str):
        """Register a function as an MCP tool. This is a decorator factory."""
        def decorator(func):
            self.tools[name] = func
            return func
        return decorator

    def start(self, host: str = "localhost", port: int = 8001):
        """Start the MCP server."""
        print(f"Starting MCP Server at {MCP_SERVER_URL}")
        uvicorn.run(self.app, host=host, port=port)


# Global MCP server instance
mcp_server = MCPServer()


def get_mcp_server():
    """Get the global MCP server instance."""
    return mcp_server


# Example of how to register a tool (this would be done in the tool files)
# @mcp_server.register_tool("example_tool")
# async def example_tool(arg1: str, arg2: int):
#     """Example tool that returns a simple response."""
#     return f"Executed example_tool with arg1={arg1}, arg2={arg2}"


if __name__ == "__main__":
    mcp_server.start()