"""
Test script to verify the Todo AI Chatbot application is running correctly
"""
import requests
import sys
import os

def test_backend():
    """Test the backend API"""
    try:
        response = requests.get("http://localhost:8000")
        if response.status_code == 200:
            print("✅ Backend API is running")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Backend API returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend API test failed: {e}")
        return False

def test_mcp_server():
    """Test the MCP server"""
    try:
        response = requests.get("http://localhost:8001")
        if response.status_code == 200:
            print("✅ MCP Server is running")
            print(f"   Response: {response.json()}")

            # Test tools endpoint
            tools_response = requests.get("http://localhost:8001/tools")
            print(f"   Available tools: {tools_response.json()['tools']}")
            return True
        else:
            print(f"❌ MCP Server returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ MCP Server test failed: {e}")
        return False

def test_api_docs():
    """Test if API documentation is accessible"""
    try:
        response = requests.get("http://localhost:8000/api/docs")
        if response.status_code == 200:
            print("✅ API Documentation is accessible")
            return True
        else:
            print(f"❌ API Documentation returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API Documentation test failed: {e}")
        return False

def main():
    print("Testing Todo AI Chatbot Application...")
    print("=" * 50)

    all_tests_passed = True

    # Test backend
    all_tests_passed &= test_backend()

    # Test MCP server
    all_tests_passed &= test_mcp_server()

    # Test API docs
    all_tests_passed &= test_api_docs()

    print("=" * 50)
    if all_tests_passed:
        print("🎉 All services are running correctly!")
        print("\nServices available:")
        print("- Backend API: http://localhost:8000")
        print("- API Documentation: http://localhost:8000/api/docs")
        print("- MCP Server: http://localhost:8001")
        print("- Frontend: http://localhost:3000 (once started)")
        print("\nThe Todo AI Chatbot is ready to use!")
    else:
        print("❌ Some services are not running correctly.")
        print("Please check the RUNNING_INSTRUCTIONS.md file for setup guidance.")
        sys.exit(1)

if __name__ == "__main__":
    main()