# Feature Specification: Backend API for Todo App with JWT Auth

**Feature Branch**: `001-backend-api-for-todo-app-with-jwt-auth`
**Created**: 2026-01-09
**Status**: Draft
**Input**: User description: "Backend API for Todo App with JWT Auth"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Secure Task Management API (Priority: P1)

As a registered user of the Todo application, I want to securely create, read, update, and delete my tasks through a REST API so that I can manage my tasks from the frontend application while ensuring my data remains private and isolated from other users.

**Why this priority**: This is the core functionality that enables the basic todo management workflow that users expect. Without this, the application has no value.

**Independent Test**: Can be fully tested by authenticating with a JWT token and performing CRUD operations on tasks, delivering complete task management functionality.

**Acceptance Scenarios**:

1. **Given** a valid JWT token for user A, **When** I make a POST request to `/api/{user_id}/tasks` with valid task data, **Then** a new task is created and associated with user A's account
2. **Given** a valid JWT token for user A and existing tasks, **When** I make a GET request to `/api/{user_id}/tasks`, **Then** I receive only tasks that belong to user A
3. **Given** a valid JWT token for user A and an existing task owned by user A, **When** I make a PUT request to `/api/{user_id}/tasks/{id}`, **Then** the task is updated successfully
4. **Given** a valid JWT token for user A and an existing task owned by user A, **When** I make a DELETE request to `/api/{user_id}/tasks/{id}`, **Then** the task is deleted successfully

---

### User Story 2 - JWT Token Validation and Authorization (Priority: P1)

As a system administrator, I want the backend API to properly validate JWT tokens and enforce user ownership so that users can only access and modify their own data and unauthorized access attempts are rejected.

**Why this priority**: Security is paramount for a multi-user system. Without proper authorization, user data could be compromised.

**Independent Test**: Can be fully tested by attempting API requests with valid/invalid/expired tokens and verifying that only properly authenticated users can access their own data.

**Acceptance Scenarios**:

1. **Given** a request without a JWT token, **When** I make any API call to `/api/{user_id}/tasks`, **Then** the system returns a 401 Unauthorized response
2. **Given** a request with an invalid/expired JWT token, **When** I make any API call to `/api/{user_id}/tasks`, **Then** the system returns a 401 Unauthorized response
3. **Given** a valid JWT token for user A, **When** I make a request to access data for user B, **Then** the system returns a 403 Forbidden response
4. **Given** a valid JWT token for user A, **When** I make a request to access data for user A, **Then** the system allows access

---

### User Story 3 - Task Completion Toggle (Priority: P2)

As a user managing my tasks, I want to be able to mark tasks as completed or incomplete so that I can track my progress and organize my workflow.

**Why this priority**: This is a core functionality that enhances the basic task management experience by allowing users to track completion status.

**Independent Test**: Can be fully tested by toggling the completion status of tasks and verifying the status updates correctly.

**Acceptance Scenarios**:

1. **Given** a valid JWT token for user A and an existing incomplete task, **When** I make a PATCH request to `/api/{user_id}/tasks/{id}/complete`, **Then** the task's completed status is toggled to true
2. **Given** a valid JWT token for user A and an existing completed task, **When** I make a PATCH request to `/api/{user_id}/tasks/{id}/complete`, **Then** the task's completed status is toggled to false

---

### Edge Cases

- What happens when a user tries to access a task that doesn't exist? (Should return 404 Not Found)
- How does the system handle requests when the database is temporarily unavailable? (Should return 500 Internal Server Error with appropriate message)
- What happens when a user sends malformed data to create/update a task? (Should return 422 Unprocessable Entity with validation errors)
- How does the system handle concurrent updates to the same task? (Should handle gracefully with appropriate locking or optimistic concurrency)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST verify JWT tokens using the BETTER_AUTH_SECRET environment variable and reject invalid or expired tokens with 401 Unauthorized
- **FR-002**: System MUST decode the user identity (user_id) from the JWT token and ensure it matches the user_id in the API route, returning 403 Forbidden if they don't match
- **FR-003**: System MUST allow users to create new tasks via POST `/api/{user_id}/tasks` with title, description, and completed status
- **FR-004**: System MUST allow users to retrieve their tasks via GET `/api/{user_id}/tasks`
- **FR-005**: System MUST allow users to retrieve a specific task via GET `/api/{user_id}/tasks/{id}`
- **FR-006**: System MUST allow users to update their tasks via PUT `/api/{user_id}/tasks/{id}`
- **FR-007**: System MUST allow users to delete their tasks via DELETE `/api/{user_id}/tasks/{id}`
- **FR-008**: System MUST allow users to toggle task completion status via PATCH `/api/{user_id}/tasks/{id}/complete`
- **FR-009**: System MUST enforce user isolation by ensuring users can only access, modify, or delete their own tasks
- **FR-010**: System MUST validate task data (title 1-200 chars, description max 1000 chars) and return appropriate error messages
- **FR-011**: System MUST return appropriate HTTP status codes for all operations (200, 201, 401, 403, 404, 422, 500)
- **FR-012**: System MUST store all data in Neon Serverless PostgreSQL using SQLModel ORM
- **FR-013**: System MUST include created_at and updated_at timestamps for all tasks

### Key Entities

- **Task**: Represents a user's todo item with properties: id (unique identifier), user_id (foreign key linking to authenticated user), title (required string 1-200 chars), description (optional string max 1000 chars), completed (boolean indicating completion status), created_at (timestamp), updated_at (timestamp)
- **User**: Represents an authenticated user identified by user_id extracted from JWT token, with associated tasks

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully create, read, update, and delete their tasks with 99.9% success rate under normal operating conditions
- **SC-002**: API responds to 95% of requests within 500ms for authenticated requests
- **SC-003**: Zero data breaches occur due to user data isolation failures over 6 months of operation
- **SC-004**: 100% of unauthorized access attempts are properly rejected with appropriate HTTP status codes
- **SC-005**: System can handle 1000 concurrent authenticated users performing CRUD operations without performance degradation
