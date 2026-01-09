# Task API Contract: Backend Service Interface

## Overview

This document defines the API contract between the frontend and backend services for task management operations. The contract specifies request/response formats, authentication requirements, and error handling patterns required for the frontend to interact with backend capabilities.

## Authentication

All endpoints require a valid JWT token issued by Better Auth:
```
Authorization: Bearer <jwt_token>
```

The JWT token must contain:
- `user_id`: The authenticated user's unique identifier
- Valid signature verified using `BETTER_AUTH_SECRET`
- Not expired (check `exp` claim)

## Base URL

```
http://localhost:8000/api  (development)
https://api.yourdomain.com/api  (production)
```

## API Endpoints

### 1. Get All User Tasks
- **Method**: GET
- **Endpoint**: `/api/{user_id}/tasks`
- **Description**: Retrieve all tasks for the authenticated user
- **Authentication**: Required (JWT token must match user_id in URL)

#### Request
```
GET /api/{user_id}/tasks
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
```

#### Successful Response (200)
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid-string",
      "user_id": "user-identifier-from-jwt",
      "title": "Task title",
      "description": "Task description",
      "completed": false,
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ],
  "message": "Tasks retrieved successfully"
}
```

#### Error Response
- **401 Unauthorized**: Missing or invalid JWT token
- **403 Forbidden**: JWT user_id does not match URL user_id
- **500 Internal Server Error**: Server error occurred

### 2. Create Task
- **Method**: POST
- **Endpoint**: `/api/{user_id}/tasks`
- **Description**: Create a new task for the authenticated user
- **Authentication**: Required (JWT token must match user_id in URL)

#### Request
```
POST /api/{user_id}/tasks
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
Body:
{
  "title": "Task title (required, 1-200 chars)",
  "description": "Task description (optional, max 1000 chars)",
  "completed": false
}
```

#### Validation Rules
- `title`: Required, 1-200 characters
- `description`: Optional, max 1000 characters if provided
- `completed`: Optional, defaults to false

#### Successful Response (201 Created)
```json
{
  "success": true,
  "data": {
    "id": "new-uuid-string",
    "user_id": "user-identifier-from-jwt",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  },
  "message": "Task created successfully"
}
```

#### Error Response
- **400 Bad Request**: Validation errors (invalid input)
- **401 Unauthorized**: Missing or invalid JWT token
- **403 Forbidden**: JWT user_id does not match URL user_id
- **422 Unprocessable Entity**: Validation errors with details
- **500 Internal Server Error**: Server error occurred

### 3. Get Specific Task
- **Method**: GET
- **Endpoint**: `/api/{user_id}/tasks/{task_id}`
- **Description**: Get a specific task for the authenticated user
- **Authentication**: Required (JWT token must match user_id in URL)

#### Request
```
GET /api/{user_id}/tasks/{task_id}
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
```

#### Successful Response (200)
```json
{
  "success": true,
  "data": {
    "id": "uuid-string",
    "user_id": "user-identifier-from-jwt",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  },
  "message": "Task retrieved successfully"
}
```

#### Error Response
- **401 Unauthorized**: Missing or invalid JWT token
- **403 Forbidden**: JWT user_id does not match URL user_id
- **404 Not Found**: Task with given ID does not exist
- **500 Internal Server Error**: Server error occurred

### 4. Update Task
- **Method**: PUT
- **Endpoint**: `/api/{user_id}/tasks/{task_id}`
- **Description**: Update an existing task for the authenticated user
- **Authentication**: Required (JWT token must match user_id in URL)

#### Request
```
PUT /api/{user_id}/tasks/{task_id}
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
Body:
{
  "title": "Updated task title (optional)",
  "description": "Updated task description (optional)",
  "completed": true
}
```

#### Successful Response (200)
```json
{
  "success": true,
  "data": {
    "id": "uuid-string",
    "user_id": "user-identifier-from-jwt",
    "title": "Updated task title",
    "description": "Updated task description",
    "completed": true,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-02T00:00:00Z"
  },
  "message": "Task updated successfully"
}
```

#### Error Response
- **400 Bad Request**: Validation errors (invalid input)
- **401 Unauthorized**: Missing or invalid JWT token
- **403 Forbidden**: JWT user_id does not match URL user_id
- **404 Not Found**: Task with given ID does not exist
- **422 Unprocessable Entity**: Validation errors with details
- **500 Internal Server Error**: Server error occurred

### 5. Delete Task
- **Method**: DELETE
- **Endpoint**: `/api/{user_id}/tasks/{task_id}`
- **Description**: Delete a task for the authenticated user
- **Authentication**: Required (JWT token must match user_id in URL)

#### Request
```
DELETE /api/{user_id}/tasks/{task_id}
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
```

#### Successful Response (200)
```json
{
  "success": true,
  "message": "Task deleted successfully"
}
```

#### Error Response
- **401 Unauthorized**: Missing or invalid JWT token
- **403 Forbidden**: JWT user_id does not match URL user_id
- **404 Not Found**: Task with given ID does not exist
- **500 Internal Server Error**: Server error occurred

### 6. Toggle Task Completion
- **Method**: PATCH
- **Endpoint**: `/api/{user_id}/tasks/{task_id}/complete`
- **Description**: Toggle the completion status of a task
- **Authentication**: Required (JWT token must match user_id in URL)

#### Request
```
PATCH /api/{user_id}/tasks/{task_id}/complete
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
```

#### Successful Response (200)
```json
{
  "success": true,
  "data": {
    "id": "uuid-string",
    "completed": true
  },
  "message": "Task completion status updated"
}
```

#### Error Response
- **401 Unauthorized**: Missing or invalid JWT token
- **403 Forbidden**: JWT user_id does not match URL user_id
- **404 Not Found**: Task with given ID does not exist
- **500 Internal Server Error**: Server error occurred

## Error Response Format

All error responses follow this format:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {
      "field": "specific field that caused error",
      "reason": "reason for the error"
    }
  }
}
```

## Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| JWT_INVALID | 401 | JWT token is invalid or malformed |
| JWT_EXPIRED | 401 | JWT token has expired |
| UNAUTHORIZED_ACCESS | 403 | User doesn't have access to this resource |
| TASK_NOT_FOUND | 404 | Task with specified ID not found |
| VALIDATION_ERROR | 422 | Request validation failed |
| SERVER_ERROR | 500 | Internal server error occurred |

## Rate Limiting

- Each user is limited to 1000 requests per hour per endpoint
- Exceeding rate limit returns HTTP 429 (Too Many Requests)

## Request/Response Formats

- **Content-Type**: All requests/responses use `application/json`
- **Timestamp Format**: ISO 8601 format (`YYYY-MM-DDTHH:MM:SSZ`)
- **ID Format**: UUID strings for all entity identifiers
- **Field Names**: Use camelCase for JSON fields (client side) but internally mapped to snake_case (Python)