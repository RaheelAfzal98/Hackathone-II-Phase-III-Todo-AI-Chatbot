#!/usr/bin/env python3
"""
Simple test to isolate the issue with the chat endpoint
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Test imports to see if there are any import errors
try:
    print("Testing imports...")

    from backend.src.services.ai_agent_service import AIAgentService
    print("[OK] AI Agent Service imported successfully")

    from backend.src.mcp_server.server import mcp_server
    print("[OK] MCP Server imported successfully")

    from backend.src.database.connection import engine
    print("[OK] Database connection imported successfully")

    # Test the OpenAI key
    import os
    api_key = os.getenv("OPENAI_API_KEY")
    print(f"[INFO] OpenAI API Key found: {'Yes' if api_key else 'No'}")

    # Try to initialize the AI agent service
    if api_key:
        ai_agent = AIAgentService(openai_api_key=api_key)
        print("[OK] AI Agent Service initialized successfully")
    else:
        print("[INFO] No API key found, but continuing...")
        # Try with a dummy key to see if it causes an error
        ai_agent = AIAgentService(openai_api_key="dummy-key")
        print("[OK] AI Agent Service initialized with dummy key")

    print("\nAll basic tests passed! The issue might be in runtime execution, not imports.")

except ImportError as e:
    print(f"[ERROR] Import error: {e}")
except Exception as e:
    print(f"[ERROR] Other error during import/test: {e}")
    import traceback
    print("Full traceback:")
    traceback.print_exc()