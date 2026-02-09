# Quickstart Guide: AI Chatbot Error Handling

## Overview
This guide provides a quick overview of how to implement and test the error handling features for the AI-powered conversational interface.

## Prerequisites
- Complete Phase II backend setup
- AI Chatbot Integration (feature 1-ai-chatbot-integration) deployed
- OpenAI API key configured
- MCP server running

## Setup Steps

### 1. Environment Configuration
```bash
# Ensure error handling settings are configured in your .env
ERROR_LOGGING_ENABLED=true
ERROR_RESPONSE_TEMPLATES_PATH=./config/error_templates.json
MONITORING_ENABLED=true
```

### 2. Database Setup
```bash
# Run database migrations to add error handling tables
# This includes the ErrorCondition, ErrorLog, and ErrorResponseTemplate tables
alembic upgrade head
```

### 3. Error Handling Configuration
```bash
# The system comes with default error templates, but you can customize them
# by modifying the templates in src/utils/error_templates.py
```

### 4. Enhanced MCP Server
```bash
# Restart the MCP server to include new error handling tools
python -m src.mcp_server.server
```

### 5. Main API Server
```bash
# Restart the main API server to enable enhanced error handling
uvicorn src.main:app --reload
```

## Testing Error Scenarios

### 1. Task Not Found Error
```bash
# Send a request for a non-existent task
curl -X POST http://localhost:8000/api/user123/chat \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"message": "Mark task 999999 as complete"}'
```

Expected response: AI agent returns a user-friendly message indicating the task doesn't exist.

### 2. Invalid Task ID Error
```bash
# Send a request with an invalid task ID format
curl -X POST http://localhost:8000/api/user123/chat \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"message": "Update task abc123xyz to new title"}'
```

Expected response: AI agent explains the correct format and asks for clarification.

### 3. Unauthorized Access Error
```bash
# Send a request attempting to access another user's task
curl -X POST http://localhost:8000/api/user123/chat \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"message": "Complete task 456"}'  # Assuming task 456 belongs to a different user
```

Expected response: AI agent indicates the task doesn't exist (without revealing it exists but belongs to someone else).

### 4. Tool Failure Error
```bash
# Simulate a tool failure scenario by temporarily stopping the MCP server
# Then send a chat request
```

Expected response: AI agent provides a fallback message indicating temporary unavailability.

## Monitoring and Logging

### View Error Logs
```bash
# Check application logs for error details
tail -f logs/app.log | grep ERROR

# Query database for error conditions
SELECT * FROM error_conditions ORDER BY timestamp DESC LIMIT 10;
```

### Check Error Statistics
The system tracks error rates and types. Monitor these metrics to identify patterns:
- Frequency of different error types
- Error response times
- User satisfaction with error handling

## Configuration Options

### Customize Error Templates
Modify `src/utils/error_templates.py` to adjust how different error types are communicated to users.

### Adjust Severity Levels
Configure how different errors are classified by modifying the error classification logic in `src/services/error_handling_service.py`.

### Enable/Disable Error Logging
Control error logging via the `ERROR_LOGGING_ENABLED` environment variable.

## Troubleshooting
- If error messages are too technical, check that `ERROR_LOGGING_ENABLED` is set to `true`
- If errors aren't being logged, verify database permissions for the error log tables
- If users report seeing internal error details, review the error sanitization in the error handling service
- If error response times are slow, check that error logging is properly configured as asynchronous

## Integration with Existing Features
- Error handling works seamlessly with existing chat functionality
- All existing authentication and authorization rules continue to apply
- Conversation history continues to be preserved during error scenarios