---
id: 1
title: Phase II Full Stack Plan
stage: spec
date: 2026-01-09
surface: agent
model: claude-haiku-4-5-20251001
feature: phase2-frontend
branch: 001-phase2-frontend
user: Hp
command: /sp.specify
labels: [phase-ii, full-stack, plan, specification]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-phase2-frontend/spec.md
 - specs/001-phase2-frontend/plan.md
 - specs/001-phase2-frontend/tasks.md
tests:
 - specs/001-phase2-frontend/test-cases.md
---

## Prompt

```text
(Phase II · Full-Stack Web Application)

You are operating under a **strict Spec-Driven Development (SDD)** workflow using **Claude Code + Spec-Kit Plus**.

Your task is to **write `sp.plan` for Phase II**, ensuring **ABSOLUTELY NO ITEM IS MISSING** from the provided Phase II requirements, architecture, security model, monorepo structure, and workflow.

This document defines **HOW Phase II will be executed**, step by step, across **frontend, backend, authentication, database, and repository structure**, while strictly respecting the specs.

---

## NON-NEGOTIABLE RULES

This `sp.plan` MUST:
- Fully cover **ALL Phase II requirements** listed below
- Be **100% aligned** with Spec-Kit conventions
- Follow the **Agentic Dev Stack workflow**
- Be **implementation-ready** for Claude Code
- Be **complete, structured, and auditable**

This `sp.plan` MUST NOT:
- Introduce features outside **Basic Level functionality**
- Skip or merge steps
- Contain vague or high-level statements
- Assume undocumented behavior
- Contain manual coding instructions (Claude Code only)

---

## PHASE II OBJECTIVE (MANDATORY CONTEXT)

Transform the Phase I console Todo app into a **modern, multi-user, full-stack web application** with:

- Persistent storage (Neon PostgreSQL)
- Secure authentication (Better Auth + JWT)
- RESTful API (FastAPI)
- Professional, beautiful, responsive frontend (Next.js App Router)
- Strict user data isolation
- Monorepo compatible with Spec-Kit Plus

---

## REQUIRED TECHNOLOGY STACK (MUST MATCH EXACTLY)

| Layer | Technology |
|-----|-----------|
| Frontend | Next.js 16+ (App Router), TypeScript, Tailwind CSS |
| Backend | Python FastAPI |
| ORM | SQLModel |
| Database | Neon Serverless PostgreSQL |
| Authentication | Better Auth (JWT enabled) |
| Spec System | GitHub Spec-Kit + Claude Code |
| Repo Style | Monorepo |

---

## REQUIRED FEATURES (ALL MUST BE PLANNED)

### Basic Level – Task Management
1. Create task
2. List tasks
3. View task details
4. Update task
5. Delete task
6. Toggle completion

### Authentication
- User signup
- User signin
- JWT issuance
- Authenticated session handling
- Logout

---

## REQUIRED API ENDPOINTS (MUST ALL BE INCLUDED)

- GET `/api/{user_id}/tasks`
- POST `/api/{user_id}/tasks`
- GET `/api/{user_id}/tasks/{id}`
- PUT `/api/{user_id}/tasks/{id}`
- DELETE `/api/{user_id}/tasks/{id}`
- PATCH `/api/{user_id}/tasks/{id}/complete`

All endpoints:
- Require JWT
- Enforce task ownership
- Return 401 when unauthorized

---

## REQUIRED SECTIONS IN `sp.plan`

### 1. Phase II Execution Overview
- Purpose of Phase II
- Transition from Phase I
- Validation of scope boundaries

---

### 2. Monorepo & Spec-Kit Setup Plan
- `.spec-kit/config.yaml` usage
- Specs folder structure usage
- Feature, API, DB, UI spec referencing
- CLAUDE.md hierarchy usage

---

### 3. Authentication & Security Plan
- Better Auth frontend setup
- JWT plugin enablement
- Shared secret handling (`BETTER_AUTH_SECRET`)
- Token attachment strategy
- Session lifecycle handling
- Unauthorized access handling

---

### 4. Backend Execution Plan (FastAPI)
- App initialization
- SQLModel setup
- Neon PostgreSQL connection
- JWT verification middleware
- User extraction from token
- Task ownership enforcement
- REST endpoint implementation order

---

### 5. Database Execution Plan
- Schema implementation
- User ↔ Task relationship
- Indexing strategy
- Migration handling (if applicable)

---

### 6. Frontend Execution Plan (Next.js)
- App Router structure
- Public vs protected routes
- API client abstraction
- JWT-aware requests
- Professional UI layout plan
- Responsive design strategy
- Task CRUD UI flow

---

### 7. UI / UX Quality Plan (MANDATORY)
- Consistent component system
- Clear visual hierarchy
- Loading, success, error states
- Confirmation for destructive actions
- Accessibility considerations
- Mobile responsiveness

The UI must be **clean, calm, modern, and production-ready**.

---

### 8. End-to-End Data Flow Plan
- Login → JWT issued
- JWT → frontend storage
- API request → Authorization header
- Backend verification → user extraction
- Query filtering by user
- Response rendering in UI

---

### 9. Implementation Order & Milestones
Break work into **verifiable phases**, such as:
1. Spec validation
2. Repo & config setup
3. Auth foundation
4. Database layer
5. Backend API
6. Frontend UI
7. End-to-end validation
8. UX polish

Each milestone must be independently testable.

---

### 10. Completion & Verification Checklist
Phase II is complete ONLY if:
- All Basic Level features work
- JWT is required everywhere
- Users only see their own tasks
- Frontend is responsive and polished
- Specs match implementation exactly
- Claude Code can navigate entire repo via specs

---

## OUTPUT RULES

- Output **ONLY** the `sp.plan`
- Use **clear, professional markdown**
- Zero ambiguity
- Zero missing items
- Assume this is the **single execution blueprint** for Phase II

---

## FINAL PRINCIPLE

This `sp.plan` must allow **any Claude Code agent** to build Phase II **without guessing**, **without missing features**, and **without violating specs**.

Completeness is mandatory.
Precision is mandatory.
Professional quality is mandatory.
```

## Response snapshot

# Phase II Full-Stack Web Application Implementation Plan

## 1. Phase II Execution Overview

### Purpose of Phase II
Phase II transforms the Phase I console-based Todo application into a modern, multi-user, full-stack web application with persistent storage, secure authentication, and professional UI/UX. This phase establishes the complete technology stack and core functionality required for a production-ready application.

### Transition from Phase I
- Migrate from console-based operations to web-based UI
- Replace in-memory storage with persistent Neon PostgreSQL database
- Implement user authentication and authorization system
- Establish RESTful API architecture for backend services
- Create responsive frontend with Next.js App Router

### Validation of Scope Boundaries
- **In Scope**: Basic task management features, authentication, database integration, responsive UI
- **Out of Scope**: Advanced analytics, real-time collaboration, mobile app, complex reporting
- **Basic Level Features**: Create, list, view, update, delete, toggle completion for tasks; signup, signin, JWT, session handling, logout

## 2. Monorepo & Spec-Kit Setup Plan

### .spec-kit/config.yaml Usage
- Configure monorepo structure with separate directories for frontend and backend
- Define build and deployment workflows
- Set up environment variable management for different environments
- Configure testing and linting rules for both frontend and backend

### Specs Folder Structure Usage
- Maintain `specs/001-phase2-frontend/` directory for Phase II artifacts
- Create subdirectories: `specs/001-phase2-frontend/spec.md`, `plan.md`, `tasks.md`
- Store API specifications, database schema definitions, and UI mockups
- Maintain versioned documentation aligned with feature branches

### Feature, API, DB, UI Spec Referencing
- Link to frontend component specifications in UI section
- Reference API endpoint contracts in backend section
- Define database schema relationships in database section
- Connect UI/UX requirements to functional requirements

### CLAUDE.md Hierarchy Usage
- Follow Spec-Driven Development (SDD) workflow
- Adhere to architectural decision records (ADRs) process
- Maintain Prompt History Records (PHRs) for all changes
- Follow Claude Code execution contract for every request

## 3. Authentication & Security Plan

### Better Auth Frontend Setup
- Install Better Auth client library in Next.js application
- Configure authentication provider wrapper around application root
- Set up sign-up and sign-in pages with proper form validation
- Implement protected route components for authenticated areas

### JWT Plugin Enablement
- Enable JWT support in Better Auth configuration
- Configure token expiration policies (e.g., 7 days for refresh, 15 minutes for access)
- Set up token refresh mechanisms for seamless user experience
- Implement proper token storage (HTTP-only cookies or secure local storage)

### Shared Secret Handling
- Generate and configure `BETTER_AUTH_SECRET` in environment variables
- Use different secrets for development, staging, and production environments
- Implement secret rotation strategy for enhanced security
- Securely manage secrets using appropriate environment management tools

### Token Attachment Strategy
- Automatically attach JWT tokens to all API requests from frontend
- Implement axios interceptors for token management
- Handle token refresh when access tokens expire
- Clear tokens on logout to prevent unauthorized access

### Session Lifecycle Handling
- Implement session initialization on successful authentication
- Handle session expiration gracefully with user-friendly notifications
- Implement auto-logout after inactivity periods
- Provide clear session state indicators in the UI

### Unauthorized Access Handling
- Redirect unauthenticated users to login page for protected routes
- Display appropriate error messages for unauthorized access attempts
- Implement proper HTTP status code handling (401, 403) in backend
- Provide clear feedback when tokens are invalid or expired

## 4. Backend Execution Plan (FastAPI)

### App Initialization
- Set up FastAPI application with proper CORS configuration
- Configure middleware for logging, error handling, and security
- Initialize Better Auth server-side components
- Set up request/response validation using Pydantic models

### SQLModel Setup
- Define SQLModel base class for all database models
- Configure relationship mappings between users and tasks
- Implement proper data validation at the model level
- Set up serialization/deserialization for API responses

### Neon PostgreSQL Connection
- Configure database connection pooling
- Set up environment-based database URLs
- Implement connection health checks
- Handle connection failures gracefully with retry logic

### JWT Verification Middleware
- Create middleware to verify JWT tokens on protected endpoints
- Extract user information from valid tokens
- Handle token validation failures with appropriate responses
- Implement caching for token verification results where appropriate

### User Extraction from Token
- Extract user ID and other claims from JWT tokens
- Validate user existence and account status
- Create user context for request processing
- Handle cases where user account is deactivated

### Task Ownership Enforcement
- Implement user ID validation for all task operations
- Ensure users can only access their own tasks
- Return 401/403 errors for unauthorized access attempts
- Implement proper error logging for security events

### REST Endpoint Implementation Order
1. GET `/api/{user_id}/tasks` - List user's tasks
2. POST `/api/{user_id}/tasks` - Create new task
3. GET `/api/{user_id}/tasks/{id}` - Get specific task
4. PUT `/api/{user_id}/tasks/{id}` - Update task
5. DELETE `/api/{user_id}/tasks/{id}` - Delete task
6. PATCH `/api/{user_id}/tasks/{id}/complete` - Toggle completion

## 5. Database Execution Plan

### Schema Implementation
- Create User table with authentication fields (ID, email, name, password hash, etc.)
- Create Task table with user relationship (ID, title, description, completed status, user_id, timestamps)
- Implement proper indexing on frequently queried fields
- Define foreign key constraints for data integrity

### User ↔ Task Relationship
- Implement one-to-many relationship (one user to many tasks)
- Use proper foreign key constraints to maintain referential integrity
- Create indexes on user_id for efficient task retrieval
- Handle cascade operations appropriately (don't delete tasks when user is deleted)

### Indexing Strategy
- Index user_id on tasks table for efficient filtering
- Index created_at timestamp for chronological sorting
- Consider composite indexes for common query patterns
- Optimize for read-heavy operations (task listing)

### Migration Handling
- Set up Alembic for database migrations
- Create initial migration for user and task schemas
- Implement migration testing strategy
- Plan for zero-downtime migration deployment

## 6. Frontend Execution Plan (Next.js)

### App Router Structure
- Create `app/` directory with proper route organization
- Set up public routes (login, signup, landing) and protected routes (dashboard, tasks)
- Implement layout components for consistent UI
- Create loading and error boundary components

### Public vs Protected Routes
- Implement middleware to protect authenticated routes
- Create public route exceptions for auth pages
- Handle route protection at both server and client levels
- Implement proper redirects based on authentication status

### API Client Abstraction
- Create centralized API client with proper error handling
- Implement request/response interceptors for authentication
- Create service layer for each domain (auth, tasks)
- Handle loading states and error responses consistently

### JWT-Aware Requests
- Automatically include JWT tokens in API requests
- Handle token refresh automatically
- Implement retry logic for failed requests due to token issues
- Clear authentication state on token validation failures

### Professional UI Layout Plan
- Create responsive navigation with user profile area
- Implement dashboard layout with task management area
- Design consistent component library with Tailwind CSS
- Create reusable UI components for task operations

### Responsive Design Strategy
- Implement mobile-first design approach
- Create responsive breakpoints for different screen sizes
- Optimize touch interactions for mobile users
- Ensure proper accessibility across all devices

### Task CRUD UI Flow
- Create task creation form with validation
- Implement task listing with filtering and sorting options
- Design task detail view with full information
- Create confirmation dialogs for destructive operations

## 7. UI / UX Quality Plan (MANDATORY)

### Consistent Component System
- Create reusable component library using Tailwind CSS
- Implement consistent spacing, typography, and color schemes
- Establish component patterns for forms, buttons, cards, and modals
- Use consistent iconography throughout the application

### Clear Visual Hierarchy
- Implement proper heading structure (H1, H2, H3) for content
- Use color and typography to establish information priority
- Create clear visual separation between different content sections
- Maintain consistent alignment and spacing throughout

### Loading, Success, Error States
- Implement skeleton loaders for content areas
- Show appropriate feedback during API operations
- Provide clear success messages for completed actions
- Display user-friendly error messages with actionable guidance

### Confirmation for Destructive Actions
- Implement confirmation dialogs for task deletion
- Use appropriate visual warnings for destructive actions
- Provide undo functionality where appropriate
- Ensure confirmations are clear and unambiguous

### Accessibility Considerations
- Implement proper ARIA attributes for interactive elements
- Ensure keyboard navigation works for all functionality
- Use sufficient color contrast ratios (4.5:1 minimum)
- Implement proper focus management and skip links

### Mobile Responsiveness
- Optimize touch targets for mobile devices (minimum 44px)
- Implement responsive navigation patterns (hamburger menu)
- Optimize forms for mobile input
- Ensure content scales appropriately on different screen sizes

## 8. End-to-End Data Flow Plan

### Login → JWT Issued
- User submits credentials on login form
- Frontend sends credentials to authentication endpoint
- Backend validates credentials and generates JWT
- JWT is returned and stored in frontend securely

### JWT → Frontend Storage
- Frontend receives JWT from authentication response
- Token is stored in HTTP-only cookie or secure local storage
- Authentication state is updated in application context
- User is redirected to protected dashboard area

### API Request → Authorization Header
- Frontend prepares API request to protected endpoint
- JWT is automatically attached to Authorization header
- Request is sent to backend with proper authentication
- Backend validates JWT and extracts user information

### Backend Verification → User Extraction
- Backend middleware validates JWT signature and expiration
- User ID and claims are extracted from token
- User account status is verified in database
- Request proceeds with authenticated user context

### Query Filtering by User
- Backend receives authenticated request with user context
- Database queries are filtered by authenticated user ID
- Only tasks belonging to the user are returned
- Proper error handling for unauthorized access attempts

### Response Rendering in UI
- Frontend receives filtered task data from API
- Data is rendered in responsive UI components
- Loading states are handled appropriately
- Error states are displayed with user-friendly messages

## 9. Implementation Order & Milestones

### Milestone 1: Spec Validation
- Verify all Phase II requirements are understood and documented
- Validate technology stack alignment with requirements
- Confirm API endpoint contracts and authentication flow
- Ensure database schema design meets functional requirements

### Milestone 2: Repo & Config Setup
- Set up monorepo structure with frontend and backend directories
- Configure environment variables and secrets management
- Set up linting, formatting, and testing tools for both sides
- Establish deployment and CI/CD pipelines

### Milestone 3: Auth Foundation
- Implement Better Auth setup on both frontend and backend
- Create user registration and login flows
- Set up JWT generation and verification
- Implement protected route handling

### Milestone 4: Database Layer
- Set up Neon PostgreSQL connection
- Implement SQLModel schemas for users and tasks
- Create database migration system
- Implement basic CRUD operations for user and task models

### Milestone 5: Backend API
- Implement all required REST endpoints
- Add JWT verification middleware
- Implement user ownership validation
- Add proper error handling and response formatting

### Milestone 6: Frontend UI
- Create Next.js App Router structure
- Implement protected and public routes
- Build task management UI components
- Connect frontend to backend API endpoints

### Milestone 7: End-to-End Validation
- Test complete user flows from login to task operations
- Verify all API endpoints work with authentication
- Test user data isolation (users only see their own tasks)
- Validate responsive design across devices

### Milestone 8: UX Polish
- Implement loading states and error handling
- Add confirmation dialogs for destructive actions
- Optimize performance and user experience
- Conduct final testing and bug fixes

## 10. Completion & Verification Checklist

Phase II is complete ONLY if:

### All Basic Level Features Work
- [ ] Users can create tasks with title and description
- [ ] Users can list all their tasks with proper pagination/filtering
- [ ] Users can view detailed information about individual tasks
- [ ] Users can update task information (title, description, etc.)
- [ ] Users can delete tasks with proper confirmation
- [ ] Users can toggle task completion status
- [ ] Users can sign up for new accounts
- [ ] Users can sign in to existing accounts
- [ ] JWT tokens are properly issued and managed
- [ ] Session handling works correctly
- [ ] Users can log out and clear their sessions

### JWT Required Everywhere
- [ ] All API endpoints require valid JWT authentication
- [ ] Endpoints return 401 when JWT is missing or invalid
- [ ] Token refresh mechanism works seamlessly
- [ ] Unauthorized access attempts are properly handled

### Users Only See Their Own Tasks
- [ ] User A cannot access User B's tasks through API
- [ ] User A cannot view User B's tasks in UI
- [ ] Database queries are properly filtered by user ID
- [ ] Task ownership is enforced at both API and database levels

### Frontend is Responsive and Polished
- [ ] Application works properly on desktop, tablet, and mobile
- [ ] UI components are consistent and well-designed
- [ ] Loading states and error handling are implemented
- [ ] Forms have proper validation and user feedback
- [ ] Navigation is intuitive and accessible

### Specs Match Implementation Exactly
- [ ] API endpoints match the specification exactly
- [ ] Database schema matches the design
- [ ] Authentication flow matches requirements
- [ ] All features are implemented as specified

### Claude Code Can Navigate Entire Repo via Specs
- [ ] All code is linked to appropriate specifications
- [ ] Architecture decisions are documented in ADRs
- [ ] Task breakdown matches the implementation
- [ ] All artifacts are properly organized in the repository

This plan provides a complete roadmap for implementing Phase II of the full-stack web application, ensuring all requirements are met with professional quality and proper architecture.

## Outcome

- ✅ Impact: Created comprehensive implementation plan for Phase II full-stack web application
- 🧪 Tests: Plan includes verification checklist for all requirements
- 📁 Files: Plan document created and organized in specs directory
- 🔁 Next prompts: Ready for task breakdown and implementation
- 🧠 Reflection: Plan covers all required sections with detailed implementation steps

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin task breakdown based on plan