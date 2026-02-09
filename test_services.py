import requests
import sys
import time

def test_service(url, service_name):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[SUCCESS] {service_name} is running at {url}")
            return True
        else:
            print(f"[ERROR] {service_name} responded with status {response.status_code} at {url}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {service_name} is not accessible at {url} - Error: {e}")
        return False

def main():
    print("Testing Todo AI Chatbot services...\n")

    services = [
        ("http://localhost:8000", "Backend API"),
        ("http://localhost:8000/health", "Backend Health Check"),
        ("http://localhost:8001", "MCP Server"),
        ("http://localhost:3000", "Frontend")
    ]

    results = {}
    for url, name in services:
        results[name] = test_service(url, name)
        time.sleep(1)  # Brief pause between requests

    print("\nSummary:")
    for name, status in results.items():
        status_text = "[SUCCESS]" if status else "[ERROR]"
        print(f"{status_text} {name}: {'Running' if status else 'Not accessible'}")

    if all(results.values()):
        print("\n[SUCCESS] All services are running successfully!")
        return True
    else:
        print("\n[WARNING] Some services are not accessible.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)