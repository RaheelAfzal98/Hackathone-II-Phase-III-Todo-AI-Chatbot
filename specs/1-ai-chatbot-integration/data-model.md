# Data Model: AI Chatbot Integration

## Overview
This document defines the data models required for the AI-powered conversational interface, extending the existing Phase II architecture with conversation and message entities while maintaining integration with existing task models.

## Entity: Conversation
**Description**: Represents a single conversation thread between user and AI assistant

### Fields
- `id` (Integer): Primary key, auto-incrementing
- `user_id` (String): Foreign key linking to authenticated user (matches Phase II user model)
- `created_at` (DateTime): Timestamp when conversation was initiated
- `updated_at` (DateTime): Timestamp of last activity in conversation
- `title` (String, Optional): Auto-generated title based on first message or topic

### Relationships
- One-to-many with Message entity (one conversation has many messages)
- Many-to-one with User entity (many conversations belong to one user)

### Validation Rules
- `user_id` must reference an existing user in the system
- `created_at` and `updated_at` are automatically managed by the system
- `title` is optional and auto-generated if not provided

## Entity: Message
**Description**: Represents individual messages within a conversation

### Fields
- `id` (Integer): Primary key, auto-incrementing
- `conversation_id` (Integer): Foreign key linking to Conversation
- `sender` (String): Enum ('user', 'assistant', 'system')
- `content` (Text): The actual message content
- `timestamp` (DateTime): When the message was sent
- `tool_calls` (JSON, Optional): Record of MCP tools called (if any)
- `tool_responses` (JSON, Optional): Responses from MCP tools (if any)

### Relationships
- Many-to-one with Conversation entity (many messages belong to one conversation)

### Validation Rules
- `conversation_id` must reference an existing conversation
- `sender` must be one of the allowed values ('user', 'assistant', 'system')
- `content` cannot be empty
- `timestamp` is automatically set when message is created

## Integration with Phase II Models
The new entities integrate with existing Phase II models as follows:

### User Model (from Phase II)
- Reused directly from Phase II authentication system
- `user_id` in Conversation entity references the same user identification as Phase II
- Authentication and authorization logic remains unchanged

### Task Model (from Phase II)
- MCP tools will interact with existing Phase II task models
- No direct changes to task model required
- Ownership validation continues to work as in Phase II

## State Transitions
- Conversation starts when user initiates first chat
- Messages are appended to conversation as interaction continues
- Conversation remains active until user ends it or system cleanup occurs
- Conversation persistence survives server restarts

## Audit Trail
- All messages are stored with timestamps
- Tool calls and responses are recorded for transparency
- User actions are linked to their authenticated identity
- All operations maintain traceability for compliance and debugging