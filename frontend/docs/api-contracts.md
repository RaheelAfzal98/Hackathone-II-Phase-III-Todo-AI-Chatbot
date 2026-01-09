# Frontend-Backend API Contracts

This document outlines the API contracts between the frontend and backend services for the Todo Management application.

## Base URL

```
http://localhost:3500/v1.0/invoke/backend/method/api/tasks
```

## Endpoints

### 1. Get All Tasks
- **Method**: GET
- **Endpoint**: `/`
- **Description**: Retrieve all tasks for the current user
- **Authentication**: Required (via JWT token in Authorization header)

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

## Error Response Format

All error responses follow this format:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message describing the issue",
    "details": {}
  }
}
```

## Common Error Codes

- `VALIDATION_ERROR`: Request validation failed
- `AUTHENTICATION_ERROR`: User authentication failed
- `AUTHORIZATION_ERROR`: User not authorized for this action
- `TASK_NOT_FOUND`: Task with given ID not found
- `TASK_FETCH_ERROR`: Error occurred while fetching tasks
- `TASK_CREATE_ERROR`: Error occurred while creating task
- `TASK_UPDATE_ERROR`: Error occurred while updating task
- `TASK_DELETE_ERROR`: Error occurred while deleting task