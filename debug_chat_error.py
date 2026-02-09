import requests
import json

def test_chat_detailed():
    """More detailed test of the chat endpoint to identify the specific error."""

    # Register a test user
    print("Step 1: Registering test user...")
    register_url = "http://localhost:8000/api/v1/register"
    register_payload = {
        "email": "test3@example.com",
        "password": "testpassword123",
        "name": "Test User 3",
        "confirm_password": "testpassword123"
    }

    try:
        register_response = requests.post(register_url, json=register_payload, timeout=10)
        print(f"Registration response: {register_response.status_code}")

        if register_response.status_code != 200:
            # Maybe user already exists, try to log in
            print("Trying to log in...")
            login_url = "http://localhost:8000/api/v1/login"
            login_payload = {
                "email": "test3@example.com",
                "password": "testpassword123"
            }

            login_response = requests.post(login_url, json=login_payload, timeout=10)
            print(f"Login response: {login_response.status_code}")

            if login_response.status_code != 200:
                print("Could not register or log in")
                return

            user_data = login_response.json()
        else:
            user_data = register_response.json()

        user_id = user_data["id"]
        token = user_data["token"]

        print(f"User ID: {user_id}")
        print(f"Token: {token[:20]}...")  # Show only first 20 chars

        # Test the chat endpoint
        print(f"\nStep 2: Testing chat endpoint for user {user_id}...")
        chat_url = f"http://localhost:8000/api/{user_id}/chat"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        payload = {
            "message": "Add a task to buy groceries",
            "conversation_id": None
        }

        print(f"Sending request to: {chat_url}")
        print(f"Headers: {headers}")
        print(f"Payload: {json.dumps(payload, indent=2)}")

        response = requests.post(chat_url, json=payload, headers=headers, timeout=30)

        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if response.status_code == 500:
            print("\n*** INTERNAL SERVER ERROR - This is the error you reported ***")
            print("The error occurs in the backend when processing the chat request.")
            print("This could be due to:")
            print("1. Missing or invalid OpenAI/OpenRouter API key in the .env file")
            print("2. MCP server not responding properly")
            print("3. Issue with the AI agent service")
        elif response.status_code == 200:
            print("\nChat endpoint worked successfully!")
            print(f"Response: {response.json()}")
        else:
            print(f"\nUnexpected status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"General error: {e}")

if __name__ == "__main__":
    test_chat_detailed()