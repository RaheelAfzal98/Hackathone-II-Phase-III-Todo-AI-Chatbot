# Data Model: Backend API for Todo App with JWT Auth

## Entity: Task

### Fields

- **id** (string/UUID): Primary key for the task
  - Type: UUID string (generated automatically)
  - Required: Yes
  - Unique: Yes
  - Validation: Must be a valid UUID format

- **user_id** (string): Foreign key linking to authenticated user
  - Type: String (user ID from JWT token)
  - Required: Yes
  - Index: Yes (for efficient user-based queries)
  - Validation: Must match the authenticated user ID

- **title** (string): Task title/description
  - Type: String
  - Required: Yes
  - Length: 1-200 characters
  - Validation: Cannot be empty or whitespace-only

- **description** (string): Detailed task description
  - Type: String (optional)
  - Required: No
  - Length: Max 1000 characters
  - Validation: Optional field with length limit

- **completed** (boolean): Completion status
  - Type: Boolean
  - Required: Yes
  - Default: False
  - Validation: Must be true or false

- **created_at** (datetime): Timestamp when task was created
  - Type: DateTime (ISO 8601 format)
  - Required: Yes
  - Auto-generated: Yes (set on creation)

- **updated_at** (datetime): Timestamp when task was last updated
  - Type: DateTime (ISO 8601 format)
  - Required: Yes
  - Auto-generated: Yes (updated on modification)

### Indexes

- `user_id`: Index on user_id field for efficient user-based queries
- `completed`: Index on completed field for efficient filtering by completion status

### Validation Rules

- Title must be between 1-200 characters
- Description, if provided, must be ≤ 1000 characters
- user_id must match the authenticated user's ID from JWT token
- completed field must be a boolean value
- All tasks must be associated with a valid user_id

### Relationships

- **User Relationship**: Each task belongs to exactly one user (identified by user_id)
- **Ownership**: Tasks are owned by the user who created them and can only be accessed by that user

### State Transitions

- **Created**: When a new task is added to the system (completed = false by default)
- **Updated**: When task details are modified (title, description, completed status)
- **Completed**: When task completion status is changed from false to true
- **Incomplete**: When task completion status is changed from true to false
- **Deleted**: When task is permanently removed from the system

## Entity: User (Virtual - from JWT)

### Fields (Extracted from JWT)

- **user_id** (string): Unique identifier for the authenticated user
  - Type: String
  - Required: Yes (for all authenticated requests)
  - Source: Extracted from JWT token payload

- **email** (string): User's email address
  - Type: String
  - Source: Extracted from JWT token payload
  - Used for identification and validation

### Validation Rules

- user_id from JWT must match the user_id in the API route
- JWT token must be valid and not expired
- User must exist in the authentication system (Better Auth)

### Relationships

- **Task Relationship**: Each user can own multiple tasks
- **Isolation**: Users can only access and modify their own tasks

## API Request/Response Models

### Task Creation Request

- **title** (string, required): Task title (1-200 chars)
- **description** (string, optional): Task description (≤1000 chars)
- **completed** (boolean, optional): Initial completion status (default: false)

### Task Response

- **id** (string): Task identifier
- **user_id** (string): Owner's user ID
- **title** (string): Task title
- **description** (string): Task description (may be null)
- **completed** (boolean): Completion status
- **created_at** (string): Creation timestamp (ISO 8601)
- **updated_at** (string): Last update timestamp (ISO 8601)

### Task Update Request

- **title** (string, optional): New task title (1-200 chars)
- **description** (string, optional): New task description (≤1000 chars)
- **completed** (boolean, optional): New completion status

### Error Response

- **detail** (string): Human-readable error message
- **status_code** (integer): HTTP status code (e.g., 401, 403, 404, 422)

## Database Schema Constraints

### Primary Keys
- Each entity has a unique primary key (id)

### Foreign Keys
- Task.user_id references the user identifier from JWT (conceptual, no actual FK constraint)

### Unique Constraints
- No unique constraints beyond primary key

### Check Constraints
- Task.title length between 1-200 characters
- Task.description length ≤ 1000 characters when provided

## Access Control Rules

### Read Access
- Users can only read tasks where user_id matches their authenticated user_id

### Write Access
- Users can only update tasks where user_id matches their authenticated user_id

### Delete Access
- Users can only delete tasks where user_id matches their authenticated user_id

### Ownership Validation
- All operations validate that the JWT user_id matches the task's user_id
- Mismatches result in 403 Forbidden responses