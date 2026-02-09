<!--
SYNC IMPACT REPORT:
Version change: 2.0.0 → 3.0.0
Modified principles: Phase 2 Architecture Non-Negotiables → AI-Native Architecture Non-Negotiables
                    Service Boundary Rules → AI-Agent Service Boundary Rules
                    Communication Rules → MCP Communication Rules
                    State Management Rules → Conversational State Management Rules
                    API Design Rules → AI-Agent API Design Rules
                    Security Constraints → AI-Specific Security Constraints
Added sections: Phase 3 Objectives, MCP Contract Enforcement, Agent Behavioral Guarantees
Removed sections: Dapr-specific rules (replaced with MCP/AI rules)
Templates requiring updates: ✅ .specify/templates/plan-template.md - updated
                             ✅ .specify/templates/spec-template.md - updated
                             ✅ .specify/templates/tasks-template.md - updated
                             ⚠️  .specify/templates/commands/*.md - pending manual review
Follow-up TODOs: None
-->
# Hackathon II Phase III AI-Powered Todo Chatbot Constitution

## Phase 3 Objectives

Phase 3 MUST transform the Phase II authenticated Todo web application into an **AI-powered conversational system** that allows users to manage their tasks using **natural language**, powered by **OpenAI Agents SDK** and **Model Context Protocol (MCP)**. This phase introduces an **AI-native architecture** where the AI agent does not manipulate the database directly but instead operates exclusively through **MCP-exposed tools**, ensuring strict separation of reasoning, actions, and state persistence.

Phase 3 is about **AI-native system design, proper separation of concerns, safe auditable AI behavior, and production-grade stateless architecture**.

## Core Principles

### AI-Native Architecture Non-Negotiables
OpenAI Agents SDK is the reasoning engine; MCP server pattern is mandatory for all AI-to-system interactions; Infrastructure access is abstracted via MCP tools; Tool-first communication is preferred over direct database access; Spec-Driven Development lifecycle is mandatory (Specify → Plan → Tasks → Implement).

### AI-Agent Service Boundary Rules
Frontend (Chat-based UI using OpenAI ChatKit) acts as a pure client with no business logic, communicating only via stateless chat API endpoint, handling UI rendering, user interaction, and API request orchestration. Backend (FastAPI + OpenAI Agents SDK + MCP Server) acts as the orchestration layer owning business rules, state transitions, and workflow coordination, remaining stateless at runtime with state persisted only via Neon PostgreSQL, exposing versioned HTTP APIs with explicit request/response schemas. AI Agent (OpenAI Agents SDK) is responsible for interpreting user intent, selecting correct MCP tools, producing friendly confirmatory responses, and must never access the database directly - all operations must be performed through MCP tools only. Each MCP tool must be stateless, deterministic, and idempotent where applicable, with ownership validation (`user_id`) performed internally.

### MCP Communication Rules
Allowed communication patterns: Frontend → Backend via authenticated HTTP requests; Backend → AI Agent via OpenAI Agents SDK; AI Agent → MCP Server via tool invocations; MCP Tools → Database via Neon PostgreSQL connector. Forbidden communication patterns: Direct database access by AI agent; Direct system calls without MCP tools; Hardcoded service URLs or ports; Cross-user data access without proper authentication and authorization checks.

### Conversational State Management Rules
Each state store has a single owning service; State access must use Neon PostgreSQL connector only; Cross-user state reads or writes are forbidden; State mutations must be explicit, idempotent where applicable, and traceable via logs/messages; All conversational context must be reconstructed from the database on each request; The server must be restart-safe without loss of conversation continuity; Conversations and messages must be persisted for traceability and audit purposes; All tool calls must be logged and returned in responses for transparency and accountability.

### AI-Agent API Design Rules
All APIs in Phase 3 MUST be explicitly versioned and define request schema, response schema, and error contract. APIs must support idempotency where retries are possible and clear error semantics, and be documented in sp.plan. The single stateless chat endpoint `POST /api/{user_id}/chat` must load conversation history from database, append new user message, execute agent with MCP tools, store assistant response, and return structured output to client without storing in-memory session state. The agent must correctly map natural language to task operations, confirm every successful action, handle errors gracefully, never hallucinate task changes without tool execution, and prefer clarification when intent is ambiguous.

### AI-Specific Security Constraints
No secrets in code or environment variables; All secrets MUST be accessed via secure configuration; Credentials and API keys are environment-specific and never hardcoded; All chat requests require valid JWT authentication (Better Auth); Every MCP tool call must be scoped to the authenticated `user_id`; Cross-user data access is strictly forbidden; Internal service calls rely on JWT-based authentication and authorization; MCP tools must validate ownership (`user_id`) internally before performing operations.

## MCP Contract Enforcement

MCP tools are the **only allowed mutation interface** for the AI agent. Tools must be stateless, deterministic, and idempotent where applicable. Tool input and output schemas must be explicitly defined. Tools must validate ownership (`user_id`) internally. The AI agent must never access the database directly. All task operations must be performed through MCP tools. The agent's only way to affect the system is via tool invocation. MCP tools are exposed using the Official MCP SDK and provide CRUD operations for tasks, conversation management, and message persistence with proper user isolation and validation at every level.

## Agent Behavioral Guarantees

The agent must: correctly map natural language to task operations; confirm every successful action; handle errors gracefully (e.g., task not found); never hallucinate task changes without tool execution; prefer clarification when intent is ambiguous; operate exclusively through MCP-exposed tools; maintain strict separation between reasoning and action; produce friendly, confirmatory responses; follow behavior rules defined in specs; remain stateless between requests; reconstruct conversational context from database on each request; ensure all operations are auditable and traceable through tool call logs; maintain user isolation and data privacy at all times; validate ownership for every operation through `user_id` scoping.

## Quality Gates

Phase 3 is considered valid ONLY if:
- Every implemented feature maps to sp.specify
- Every architectural decision maps to sp.plan
- Every code change references a Task ID
- Every user interaction triggers a backend capability
- Every AI operation goes through MCP tools
- Every conversation is persisted and reconstructible
- Every tool call is logged and auditable

No task = No code.

## Explicitly Forbidden

Agents and humans MUST NOT:
- Implement features without acceptance criteria
- Bypass the Spec-Kit lifecycle
- Allow AI agent direct database access
- Introduce speculative or future-phase features
- Modify Phase 1/2 architecture decisions without proper justification
- Access infrastructure directly without MCP tools
- Perform operations without proper user authentication and authorization
- Store in-memory session state for conversations
- Allow cross-user data access without proper validation

If ambiguous requirements are encountered, consult the specification or request clarification before proceeding.

## Governance

This constitution governs how agents and humans are allowed to design, plan, and implement Phase 3. All architectural decisions must align with these principles. Changes to this constitution require explicit approval and documentation of the rationale. The constitution supersedes all other development practices and serves as the ultimate authority for architectural decisions during Phase 3 implementation. This version introduces AI-specific governance requirements, MCP contract enforcement, and agent behavioral guarantees that were not present in Phase 2 with Dapr architecture. The shift from Dapr-based services to MCP/AI-agent architecture represents a significant architectural evolution for this phase while maintaining the core Spec-Driven Development principles established in previous phases.

**Version**: 3.0.0 | **Ratified**: 2026-01-20 | **Last Amended**: 2026-01-20