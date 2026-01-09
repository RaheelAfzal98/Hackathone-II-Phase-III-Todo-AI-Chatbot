# Data Model: Phase 2 Frontend - Todo Management UI

## Task Entity

### Fields
- **id** (string): Unique identifier for the task
  - Type: String (UUID format)
  - Required: Yes
  - Validation: Must be a valid UUID format
- **title** (string): Task title/description
  - Type: String
  - Required: Yes
  - Validation: 1-255 characters, no leading/trailing whitespace
- **description** (string): Detailed task description
  - Type: String
  - Required: No
  - Validation: 0-1000 characters
- **completed** (boolean): Completion status
  - Type: Boolean
  - Required: Yes
  - Default: false
- **priority** (string): Task priority level
  - Type: Enum ['low', 'medium', 'high']
  - Required: Yes
  - Default: 'medium'
- **createdAt** (datetime): Creation timestamp
  - Type: ISO 8601 datetime string
  - Required: Yes
  - Read-only: Backend-generated
- **updatedAt** (datetime): Last update timestamp
  - Type: ISO 8601 datetime string
  - Required: Yes
  - Read-only: Backend-generated

### Relationships
- None (standalone entity)

### Validation Rules
- Title must not be empty or consist only of whitespace
- Priority must be one of the allowed values
- Description length must not exceed 1000 characters
- ID must be a valid UUID format

### State Transitions
- **Active** → **Completed**: When user marks task as complete
- **Completed** → **Active**: When user unmarks task completion
- **Created**: New task added to the system
- **Deleted**: Task removed from the system

## UI State Models

### Filter State
- **statusFilter** (string): Current status filter
  - Type: Enum ['all', 'active', 'completed']
  - Default: 'all'
- **priorityFilter** (string): Current priority filter
  - Type: Enum ['all', 'low', 'medium', 'high']
  - Default: 'all'
- **searchQuery** (string): Current search term
  - Type: String
  - Default: ''

### Form State
- **isSubmitting** (boolean): Whether form is currently submitting
  - Type: Boolean
  - Default: false
- **errors** (object): Field-specific validation errors
  - Type: Object with field names as keys
  - Default: {}

### Toast State
- **show** (boolean): Whether toast is visible
  - Type: Boolean
  - Default: false
- **message** (string): Toast message content
  - Type: String
- **type** (string): Toast type
  - Type: Enum ['success', 'error', 'info', 'warning']
- **duration** (number): Auto-dismiss duration in ms
  - Type: Number
  - Default: 5000

## API Response Models

### Task Response
- **data** (object or array): Task data or tasks array
- **success** (boolean): Whether request succeeded
- **message** (string): Optional human-readable message
- **errors** (array): Array of error objects if request failed
  - Each error has: `field`, `message`

### Error Response
- **error** (object):
  - **code** (string): Machine-readable error code
  - **message** (string): Human-readable error message
  - **details** (object): Additional error details

## Component Props Models

### TaskCard Props
- **task** (object): Task object (as defined above)
- **onToggleComplete** (function): Handler for completion toggle
- **onDelete** (function): Handler for task deletion
- **onEdit** (function): Handler for task editing

### TaskForm Props
- **initialData** (object): Initial form data (optional)
- **onSubmit** (function): Submission handler
- **onCancel** (function): Cancel handler (optional)
- **submitText** (string): Text for submit button
  - Default: "Add Task" or "Update Task"

### TaskList Props
- **tasks** (array): Array of task objects
- **loading** (boolean): Whether tasks are loading
- **emptyMessage** (string): Message to show when no tasks
  - Default: "No tasks found"

## Accessibility Attributes

### Keyboard Navigation
- **tabIndex** (number): Element tab order
- **aria-label** (string): Accessible label for unlabeled elements
- **aria-describedby** (string): Reference to descriptive element
- **role** (string): ARIA role for custom components

### Focus Management
- **focusKey** (string): Key to manage focus state
- **focused** (boolean): Whether element currently has focus