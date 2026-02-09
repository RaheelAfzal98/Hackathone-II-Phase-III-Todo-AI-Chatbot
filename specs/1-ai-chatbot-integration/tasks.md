# Implementation Tasks: AI Chatbot Integration

**Feature**: AI Chatbot Integration | **Date**: 2026-01-08 | **Spec**: [link](./spec.md) | **Plan**: [link](./plan.md)

## Implementation Strategy

**MVP Scope**: User Story 1 - Basic chat functionality with add_task MCP tool
**Delivery Approach**: Incremental delivery with each user story as a complete, independently testable increment
**Priority Order**: Based on spec.md user story priorities

---

## Phase 1: Setup

**Goal**: Initialize project structure and dependencies for AI chatbot integration

- [X] T001 Create backend/src/mcp_server directory structure
- [X] T002 Create backend/src/models/conversation.py and backend/src/models/message.py
- [X] T003 Create backend/src/services/conversation_service.py and backend/src/services/ai_agent_service.py
- [X] T004 Create backend/src/api/chat_endpoint.py
- [X] T005 Install and configure MCP server dependencies in backend requirements.txt
- [X] T006 Set up frontend/src/components/ChatInterface.jsx structure

## Phase 2: Foundational

**Goal**: Implement core infrastructure and shared components that block all user stories

- [X] T007 Implement Conversation model with fields per data-model.md in backend/src/models/conversation.py
- [X] T008 Implement Message model with fields per data-model.md in backend/src/models/message.py
- [X] T009 Create database migration for new conversation and message tables
- [X] T010 Implement ConversationService with CRUD operations in backend/src/services/conversation_service.py
- [X] T011 Implement authentication middleware for chat endpoint using Better Auth
- [X] T012 Create MCP server initialization in backend/src/mcp_server/server.py
- [X] T013 Set up OpenAI Agent SDK configuration and initialization

## Phase 3: [US1] Primary User Scenario - Add Task via Natural Language

**Goal**: Enable users to add tasks using natural language (e.g., "Add a task to buy groceries")

**Independent Test Criteria**: User can send natural language message to add a task and receive confirmation response

- [X] T014 [P] [US1] Implement add_task MCP tool in backend/src/mcp_server/tools/add_task.py
- [X] T015 [P] [US1] Implement chat endpoint POST /api/{user_id}/chat in backend/src/api/chat_endpoint.py
- [X] T016 [US1] Create conversation when none exists in chat endpoint
- [X] T017 [US1] Save user message to conversation in Message model
- [X] T018 [US1] Initialize OpenAI Agent with add_task tool
- [X] T019 [US1] Process user input through AI agent to select add_task tool
- [X] T020 [US1] Execute add_task MCP tool with proper user_id scoping
- [X] T021 [US1] Save AI response to conversation in Message model
- [X] T022 [US1] Return structured response with conversation_id, response, and tool_calls
- [X] T023 [US1] Create basic ChatInterface component in frontend/src/components/ChatInterface.jsx
- [X] T024 [US1] Connect ChatInterface to chat API endpoint in frontend/src/services/chat_api.js
- [X] T025 [US1] Test full flow: user message → AI processing → tool execution → response

## Phase 4: [US2] Secondary User Scenario - List Tasks via Natural Language

**Goal**: Enable users to list tasks using natural language (e.g., "Show my tasks")

**Independent Test Criteria**: User can send natural language message to list tasks and receive response with task list

- [X] T026 [P] [US2] Implement list_tasks MCP tool in backend/src/mcp_server/tools/list_tasks.py
- [X] T027 [US2] Extend OpenAI Agent configuration to include list_tasks tool
- [X] T028 [US2] Process user input through AI agent to select list_tasks tool
- [X] T029 [US2] Execute list_tasks MCP tool with proper user_id scoping
- [X] T030 [US2] Format task list in AI response
- [X] T031 [US2] Test full flow: "Show my tasks" → AI processing → list_tasks tool → response with tasks

## Phase 5: [US3] Secondary User Scenario - Complete Task via Natural Language

**Goal**: Enable users to mark tasks as complete using natural language (e.g., "Mark task 3 complete")

**Independent Test Criteria**: User can send natural language message to complete a task and receive confirmation

- [X] T032 [P] [US3] Implement complete_task MCP tool in backend/src/mcp_server/tools/complete_task.py
- [X] T033 [US3] Extend OpenAI Agent configuration to include complete_task tool
- [X] T034 [US3] Process user input through AI agent to select complete_task tool
- [X] T035 [US3] Execute complete_task MCP tool with proper user_id scoping and validation
- [X] T036 [US3] Test full flow: "Mark task 3 complete" → AI processing → complete_task tool → confirmation

## Phase 6: [US4] Secondary User Scenario - Update Task via Natural Language

**Goal**: Enable users to update tasks using natural language (e.g., "Change the title of task 1 to 'buy milk'")

**Independent Test Criteria**: User can send natural language message to update a task and receive confirmation

- [X] T037 [P] [US4] Implement update_task MCP tool in backend/src/mcp_server/tools/update_task.py
- [X] T038 [US4] Extend OpenAI Agent configuration to include update_task tool
- [X] T039 [US4] Process user input through AI agent to select update_task tool
- [X] T040 [US4] Execute update_task MCP tool with proper user_id scoping and validation
- [X] T041 [US4] Test full flow: "Change title of task 1" → AI processing → update_task tool → confirmation

## Phase 7: [US5] Secondary User Scenario - Delete Task via Natural Language

**Goal**: Enable users to delete tasks using natural language (e.g., "Delete task 2")

**Independent Test Criteria**: User can send natural language message to delete a task and receive confirmation

- [X] T042 [P] [US5] Implement delete_task MCP tool in backend/src/mcp_server/tools/delete_task.py
- [X] T043 [US5] Extend OpenAI Agent configuration to include delete_task tool
- [X] T044 [US5] Process user input through AI agent to select delete_task tool
- [X] T045 [US5] Execute delete_task MCP tool with proper user_id scoping and validation
- [X] T046 [US5] Test full flow: "Delete task 2" → AI processing → delete_task tool → confirmation

## Phase 8: [US6] Conversation Persistence & Continuity

**Goal**: Ensure conversation history is persisted and reconstructed for continuity across sessions

**Independent Test Criteria**: Conversation state is maintained across multiple requests and server restarts

- [X] T047 [P] [US6] Implement conversation loading logic in chat endpoint
- [X] T048 [US6] Extend chat endpoint to accept existing conversation_id parameter
- [X] T049 [US6] Test conversation continuity: multiple messages in same conversation
- [X] T050 [US6] Verify conversation persistence survives server restarts
- [X] T051 [US6] Add conversation history to AI agent context for continuity

## Phase 9: [US7] Error Handling & Validation

**Goal**: Handle edge cases and provide appropriate error responses per requirements

**Independent Test Criteria**: System handles invalid inputs, unauthorized access, and network issues gracefully

- [X] T052 [P] [US7] Implement validation for invalid task IDs in MCP tools
- [X] T053 [US7] Add proper error handling for unauthorized access attempts
- [X] T054 [US7] Create error responses that don't reveal sensitive information
- [X] T055 [US7] Handle natural language that cannot be mapped to actions
- [X] T056 [US7] Test error scenarios and confirm appropriate user-friendly responses

## Phase 10: Polish & Cross-Cutting Concerns

**Goal**: Final integration, testing, and polish to ensure all requirements are met

- [X] T057 Implement tool call and response logging in Message model (tool_calls, tool_responses fields)
- [X] T058 Add performance monitoring to ensure <5 second response time
- [X] T059 Conduct security review to ensure no direct AI database access
- [X] T060 Verify all Phase II functionality remains unchanged
- [X] T061 Test concurrent chat sessions for different users
- [X] T062 Update frontend ChatInterface with improved UX based on all user stories
- [X] T063 Conduct end-to-end testing of all user scenarios
- [X] T064 Verify 95% success rate for natural language processing
- [X] T065 Document API usage and integration points

---

## Dependencies

**User Story Dependency Graph**:
- Phase 2 (Foundational) must complete before any user story phases
- US1 (Add Task) should complete before US2-US5 (provides basic infrastructure)
- US2-US5 can run in parallel after US1 completion
- US6 (Conversation Persistence) can run in parallel with US2-US5
- US7 (Error Handling) can run in parallel with other user stories
- Phase 10 requires all other phases to complete

## Parallel Execution Opportunities

**Tasks that can run in parallel** (marked with [P]):
- MCP tool implementations (T014, T026, T032, T037, T042) - each in separate files
- Initial component creation (backend/frontend components simultaneously)

**Recommended Parallel Execution per User Story**:
- US1: T014 and T015 can run in parallel (tool and endpoint)
- US2-US5: All MCP tool implementations can run in parallel (different files)
- US7: All validation tasks can run in parallel (different error scenarios)

## Test Cases

**MVP Test Case (US1)**: As a user, I can send "Add a task to buy groceries" and receive confirmation that the task was added to my list.

**Full Feature Test Case**: As a user, I can manage all my tasks through natural language commands (add, list, complete, update, delete) with proper authentication and error handling.