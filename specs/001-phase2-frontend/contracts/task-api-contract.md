# Task API Contract: Frontend ↔ Backend Communication

## Overview
This document defines the API contract between the frontend and backend services for task management operations. The contract specifies request/response formats, error handling, and communication patterns required for the frontend to interact with backend capabilities via Dapr service invocation.

## Base URL
```
http://localhost:3500/v1.0/invoke/backend/method/api/tasks
```

## API Endpoints

### 1. Get All Tasks
- **Method**: GET
- **Endpoint**: `/`
- **Description**: Retrieve all tasks for the current user
- **Authentication**: Required (via Dapr authentication)

#### Request
```
GET /v1.0/invoke/backend/method/api/tasks
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
```

#### Response
- **Success (200)**:
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid-string",
      "title": "Task title",
      "description": "Task description",
      "completed": false,
      "priority": "high|medium|low",
      "createdAt": "2023-01-01T00:00:00Z",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ],
  "message": "Tasks retrieved successfully"
}
```

- **Error (4xx/5xx)**:
```json
{
  "success": false,
  "error": {
    "code": "TASK_FETCH_ERROR",
    "message": "Error message describing the issue",
    "details": {}
  }
}
```

### 2. Create Task
- **Method**: POST
- **Endpoint**: `/`
- **Description**: Create a new task

#### Request
```
POST /v1.0/invoke/backend/method/api/tasks
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
Body:
{
  "title": "Task title (required)",
  "description": "Task description (optional)",
  "priority": "high|medium|low (default: medium)"
}
```

#### Response
- **Success (201)**:
```json
{
  "success": true,
  "data": {
    "id": "uuid-string",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "priority": "high|medium|low",
    "createdAt": "2023-01-01T00:00:00Z",
    "updatedAt": "2023-01-01T00:00:00Z"
  },
  "message": "Task created successfully"
}
```

- **Validation Error (400)**:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "One or more validation errors occurred",
    "details": {
      "errors": [
        {
          "field": "title",
          "message": "Title is required and must be between 1 and 255 characters"
        }
      ]
    }
  }
}
```

### 3. Update Task
- **Method**: PUT
- **Endpoint**: `/{taskId}`
- **Description**: Update an existing task

#### Request
```
PUT /v1.0/invoke/backend/method/api/tasks/{taskId}
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
Body:
{
  "title": "Updated task title (optional)",
  "description": "Updated task description (optional)",
  "completed": true|false (optional),
  "priority": "high|medium|low (optional)"
}
```

#### Response
- **Success (200)**:
```json
{
  "success": true,
  "data": {
    "id": "uuid-string",
    "title": "Updated task title",
    "description": "Updated task description",
    "completed": true,
    "priority": "high",
    "createdAt": "2023-01-01T00:00:00Z",
    "updatedAt": "2023-01-02T00:00:00Z"
  },
  "message": "Task updated successfully"
}
```

### 4. Toggle Task Completion
- **Method**: PATCH
- **Endpoint**: `/{taskId}/toggle-complete`
- **Description**: Toggle the completion status of a task

#### Request
```
PATCH /v1.0/invoke/backend/method/api/tasks/{taskId}/toggle-complete
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
```

#### Response
- **Success (200)**:
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

### 5. Delete Task
- **Method**: DELETE
- **Endpoint**: `/{taskId}`
- **Description**: Delete a task

#### Request
```
DELETE /v1.0/invoke/backend/method/api/tasks/{taskId}
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
```

#### Response
- **Success (200)**:
```json
{
  "success": true,
  "message": "Task deleted successfully"
}
```

### 6. Filter Tasks
- **Method**: GET
- **Endpoint**: `/filter`
- **Description**: Get tasks with filtering options

#### Request
```
GET /v1.0/invoke/backend/method/api/tasks/filter?status=active&priority=high&search=term
Headers:
  Authorization: Bearer {token}
  Content-Type: application/json
Query Parameters:
  - status: all|active|completed (optional)
  - priority: all|high|medium|low (optional)
  - search: search term (optional)
```

#### Response
- **Success (200)**:
```json
{
  "success": true,
  "data": [
    // Array of task objects matching the filter
  ],
  "filtersApplied": {
    "status": "active",
    "priority": "high",
    "search": "term"
  },
  "message": "Filtered tasks retrieved successfully"
}
```

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| VALIDATION_ERROR | 400 | Request validation failed |
| AUTHENTICATION_ERROR | 401 | User authentication failed |
| AUTHORIZATION_ERROR | 403 | User not authorized for this action |
| TASK_NOT_FOUND | 404 | Task with given ID not found |
| TASK_FETCH_ERROR | 500 | Error occurred while fetching tasks |
| TASK_CREATE_ERROR | 500 | Error occurred while creating task |
| TASK_UPDATE_ERROR | 500 | Error occurred while updating task |
| TASK_DELETE_ERROR | 500 | Error occurred while deleting task |

## Communication Patterns

### Request Format
- All requests use JSON format
- Content-Type header set to `application/json`
- Authentication via Bearer token in Authorization header
- All endpoints follow REST conventions

### Response Format
- All responses follow the same structure with `success`, `data`, and `message` fields
- Errors follow the same structure with `error` object containing `code`, `message`, and optional `details`
- Success responses use appropriate HTTP status codes (200, 201)
- Error responses use appropriate HTTP status codes (4xx, 5xx)

## Dapr-Specific Headers
When making service invocations through Dapr, the following headers may be automatically handled:
- `dapr-app-id`: Identifies the target application
- `dapr-method`: The method being invoked
- These are handled by the Dapr service invocation mechanism

## Performance Expectations
- API responses should be delivered within 2 seconds
- Task creation/update/deletion operations should complete within 2 seconds
- Bulk operations (like getting all tasks) should complete within 3 seconds for up to 100 tasks
- Error responses should be returned within 1 second