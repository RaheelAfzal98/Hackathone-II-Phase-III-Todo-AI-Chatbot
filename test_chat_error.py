import requests
import json

def test_chat_endpoint():
    """Test the chat endpoint to reproduce the error."""

    # Assuming we have a logged in user - we'll need a valid user ID
    # For testing, let's first create a test user or use an existing one
    print("Testing chat endpoint...")

    # First, let's try to make a simple request to the chat endpoint
    # We'll need a valid user ID - for now let's try with a placeholder
    user_id = "test_user_123"  # This would normally come from authentication

    # Try to make a request to the chat endpoint
    chat_url = f"http://localhost:8000/api/{user_id}/chat"

    headers = {
        "Content-Type": "application/json",
        # In a real scenario, you'd need an Authorization header with a valid JWT
        # "Authorization": "Bearer <valid_jwt_token>"
    }

    payload = {
        "message": "Add a task to buy groceries",
        "conversation_id": None
    }

    try:
        print(f"Making request to: {chat_url}")
        print(f"Payload: {json.dumps(payload, indent=2)}")

        response = requests.post(chat_url, json=payload, headers=headers, timeout=30)

        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Body: {response.text}")

        if response.status_code == 200:
            print("Success! Chat endpoint worked.")
            return True
        else:
            print("Error occurred with the chat endpoint.")
            return False

    except requests.exceptions.ConnectionError:
        print("Could not connect to the backend server. Is it running?")
        return False
    except requests.exceptions.Timeout:
        print("Request timed out. The server might be taking too long to respond.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False

def test_with_auth():
    """Test with authentication - try to get a token first."""
    print("\nTrying to authenticate first...")

    # Try to register a test user
    register_url = "http://localhost:8000/api/v1/auth/register"
    register_payload = {
        "email": "test@example.com",
        "password": "testpassword123"
    }

    try:
        response = requests.post(register_url, json=register_payload, timeout=10)
        print(f"Registration response: {response.status_code} - {response.text[:200]}...")

        if response.status_code in [200, 201, 400, 409]:  # 400/409 might indicate user exists
            # Try to login
            login_url = "http://localhost:8000/api/v1/auth/login"
            login_payload = {
                "email": "test@example.com",
                "password": "testpassword123"
            }

            response = requests.post(login_url, json=login_payload, timeout=10)
            print(f"Login response: {response.status_code}")

            if response.status_code == 200:
                response_json = response.json()
                token = response_json.get("access_token")
                if token:
                    print("Got authentication token, now testing chat endpoint...")

                    # Test chat endpoint with auth
                    user_id = response_json.get("user_id", "test_user_123")
                    chat_url = f"http://localhost:8000/api/{user_id}/chat"

                    headers = {
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {token}"
                    }

                    payload = {
                        "message": "Add a task to buy groceries",
                        "conversation_id": None
                    }

                    chat_response = requests.post(chat_url, json=payload, headers=headers, timeout=30)
                    print(f"Authenticated chat response: {chat_response.status_code}")
                    print(f"Response: {chat_response.text}")
                    return True
                else:
                    print("No token in login response")
            else:
                print(f"Login failed: {response.text}")

    except Exception as e:
        print(f"Authentication test failed: {e}")
        # Continue with chat test anyway

    return False

if __name__ == "__main__":
    print("Testing the chat error...")

    # Test without auth first (might fail due to auth requirement)
    success = test_chat_endpoint()

    if not success:
        # Try with auth
        test_with_auth()