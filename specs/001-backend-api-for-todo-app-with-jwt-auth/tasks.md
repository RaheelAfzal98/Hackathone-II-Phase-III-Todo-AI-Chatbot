# Tasks: Backend API for Todo App with JWT Auth

**Feature**: Backend API for Todo App with JWT Auth
**Branch**: `001-backend-api-for-todo-app-with-jwt-auth`
**Created**: 2026-01-09
**Input**: Implementation plan and feature specification

## Implementation Strategy

**MVP Scope**: Complete User Story 1 (Secure Task Management API) with basic JWT authentication, task CRUD operations, and user isolation. This will deliver a fully functional task management backend that can be independently tested and demonstrated.

**Approach**: Build incrementally following the user story priorities (P1, P2, P3) with each story being independently testable and providing complete functionality for that specific user journey.

## Dependencies

- User Story 2 (JWT Auth) must be implemented before User Story 1 (Task Management) for the authentication infrastructure
- User Story 3 (Task Completion Toggle) depends on User Story 1 (Task Management) for the base task operations

## Parallel Execution Opportunities

- Authentication infrastructure components can be developed in parallel [P]
- API endpoint implementations can be developed in parallel after foundational components are complete [P]
- Testing can be done in parallel with implementation [P]

---

## Phase 1: Setup

### Goal
Initialize the Python/FastAPI project with proper configuration and dependencies to support the backend architecture.

- [x] T001 Create backend directory structure per implementation plan
- [x] T002 Initialize Python project with pyproject.toml and requirements.txt
- [x] T003 [P] Install and configure FastAPI framework with async support
- [x] T004 [P] Install and configure SQLModel ORM for database operations
- [x] T005 [P] Install and configure PyJWT for JWT token handling
- [x] T006 [P] Install and configure psycopg2-binary for PostgreSQL connectivity
- [x] T007 Configure Python project settings and environment management
- [x] T008 Create .env.example file with required environment variables
- [x] T009 Create .gitignore file with Python/PyCharm patterns
- [x] T010 Set up basic project configuration in src/config/settings.py

---

## Phase 2: Foundational Components

### Goal
Create foundational components and service layers that will be used across all user stories.

- [x] T011 Create base SQLModel with common fields (id, created_at, updated_at) in src/models/base.py
- [x] T012 [P] Create database connection module in src/database/connection.py
- [x] T013 [P] Create database session management in src/database/session.py
- [x] T014 [P] Create JWT token verification utility in src/auth/jwt_handler.py
- [x] T015 [P] Create authentication dependencies for FastAPI in src/auth/dependencies.py
- [x] T016 Create custom exception classes in src/utils/exceptions.py
- [x] T017 Create utility functions in src/utils/helpers.py
- [x] T018 Create API version 1 router in src/api/v1/__init__.py
- [x] T019 Create API endpoints router in src/api/v1/endpoints/__init__.py
- [x] T020 Create main FastAPI application in main.py

---

## Phase 3: User Story 1 - Secure Task Management API (Priority: P1)

### Goal
Implement the core task management functionality allowing users to create, read, update, and delete tasks with user isolation.

**Independent Test Criteria**: User can authenticate with JWT token and perform all CRUD operations on their tasks while being prevented from accessing other users' tasks.

- [x] T021 [US1] Create Task model definition in src/models/task.py
- [x] T022 [US1] Create Task schemas (create, update, response) in src/schemas/task.py
- [x] T023 [US1] Create TaskService for business logic in src/services/task_service.py
- [x] T024 [US1] Implement task creation endpoint POST /api/{user_id}/tasks in src/api/v1/endpoints/tasks.py
- [x] T025 [US1] Implement task retrieval endpoint GET /api/{user_id}/tasks in src/api/v1/endpoints/tasks.py
- [x] T026 [US1] Implement specific task retrieval endpoint GET /api/{user_id}/tasks/{id} in src/api/v1/endpoints/tasks.py
- [x] T027 [US1] Implement task update endpoint PUT /api/{user_id}/tasks/{id} in src/api/v1/endpoints/tasks.py
- [x] T028 [US1] Implement task deletion endpoint DELETE /api/{user_id}/tasks/{id} in src/api/v1/endpoints/tasks.py
- [x] T029 [US1] Add user isolation enforcement to all task endpoints
- [x] T030 [US1] Implement proper validation for task data (title 1-200 chars, description max 1000 chars)
- [x] T031 [US1] Add proper HTTP status codes for all operations (200, 201, 404, 422)
- [x] T032 [US1] Create integration tests for task CRUD operations
- [x] T033 [US1] Test user isolation (user A cannot access user B's tasks)
- [x] T034 [US1] Verify data persistence in Neon PostgreSQL database

---

## Phase 4: User Story 2 - JWT Token Validation and Authorization (Priority: P1)

### Goal
Implement JWT token validation and enforce user ownership to ensure users can only access and modify their own data.

**Independent Test Criteria**: System properly validates JWT tokens and rejects unauthorized access attempts with appropriate HTTP status codes.

- [x] T035 [US2] Enhance JWT token verification to validate BETTER_AUTH_SECRET in src/auth/jwt_handler.py
- [x] T036 [US2] Implement JWT token expiry validation in src/auth/jwt_handler.py
- [x] T037 [US2] Create authentication dependency that extracts user_id from JWT token
- [x] T038 [US2] Implement user_id matching validation (JWT vs URL)
- [x] T039 [US2] Return 401 Unauthorized for missing/invalid JWT tokens
- [x] T040 [US2] Return 403 Forbidden for user_id mismatches
- [x] T041 [US2] Add JWT validation to all API endpoints
- [x] T042 [US2] Create JWT validation tests in tests/test_auth/
- [x] T043 [US2] Test invalid/expired token scenarios
- [x] T044 [US2] Test cross-user access prevention
- [x] T045 [US2] Verify proper error responses for all auth scenarios

---

## Phase 5: User Story 3 - Task Completion Toggle (Priority: P2)

### Goal
Enable users to mark tasks as completed or incomplete to track progress and organize workflow.

**Independent Test Criteria**: User can toggle completion status of their tasks via PATCH endpoint while preventing access to other users' tasks.

- [x] T046 [US3] Implement task completion toggle endpoint PATCH /api/{user_id}/tasks/{id}/complete in src/api/v1/endpoints/tasks.py
- [x] T047 [US3] Add toggle logic to TaskService in src/services/task_service.py
- [x] T048 [US3] Ensure completion toggle respects user isolation
- [x] T049 [US3] Return proper response format for completion toggle
- [x] T050 [US3] Add completion toggle validation
- [x] T051 [US3] Create tests for completion toggle functionality
- [x] T052 [US3] Test toggle from incomplete to complete
- [x] T053 [US3] Test toggle from complete to incomplete
- [x] T054 [US3] Verify completion status persistence

---

## Phase 6: Error Handling & Response Consistency

### Goal
Ensure consistent error responses and proper HTTP status codes across all endpoints.

- [x] T055 Create standardized error response format in src/schemas/error.py
- [x] T056 Implement HTTPException handling for 401 Unauthorized responses
- [x] T057 Implement HTTPException handling for 403 Forbidden responses
- [x] T058 Implement HTTPException handling for 404 Not Found responses
- [x] T059 Implement HTTPException handling for 422 Validation Error responses
- [x] T060 Add structured logging for all operations
- [x] T061 Create error handling tests in tests/test_api/
- [x] T062 Verify all error scenarios return appropriate JSON responses

---

## Phase 7: Middleware & Security Configuration

### Goal
Configure security measures and middleware for production readiness.

- [x] T063 Configure CORS middleware for frontend origin in main.py
- [x] T064 Implement rate limiting per user (1000 requests/hour)
- [x] T065 Add request/response logging middleware
- [x] T066 Configure security headers for API responses
- [x] T067 Test security configurations
- [x] T068 Verify rate limiting functionality

---

## Phase 8: Testing & Verification

### Goal
Ensure all functionality works as expected and meets quality standards.

- [x] T069 Write unit tests for Task model and schemas
- [x] T070 [P] Write unit tests for authentication utilities
- [x] T071 [P] Write unit tests for TaskService
- [x] T072 [P] Write integration tests for all API endpoints
- [x] T073 Create test factories for Task entities
- [x] T074 Run all tests with 90%+ coverage
- [x] T075 Perform security testing for auth bypass attempts
- [x] T076 Verify all acceptance criteria from spec are met
- [x] T077 Test concurrent access scenarios
- [x] T078 Performance test for response times under load

---

## Phase 9: Documentation & Polish

### Goal
Complete documentation and final quality checks.

- [x] T079 Update API documentation with proper examples
- [x] T080 Add inline code documentation for complex components
- [x] T081 Create deployment configuration files
- [x] T082 Optimize database queries and add proper indexing
- [x] T083 Perform final security review
- [x] T084 Verify all edge cases are handled properly
- [x] T085 Update quickstart guide with latest implementation details
- [x] T086 Run final end-to-end tests
- [x] T087 Verify all success criteria from spec are met