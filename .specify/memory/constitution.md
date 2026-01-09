<!--
SYNC IMPACT REPORT:
Version change: [CONSTITUTION_VERSION] → 2.0.0
Modified principles: [PRINCIPLE_1_NAME] → Phase 2 Architecture Non-Negotiables
                    [PRINCIPLE_2_NAME] → Service Boundary Rules
                    [PRINCIPLE_3_NAME] → Communication Rules
                    [PRINCIPLE_4_NAME] → State Management Rules
                    [PRINCIPLE_5_NAME] → API Design Rules
                    [PRINCIPLE_6_NAME] → Security Constraints
Added sections: Phase 2 Objectives, Observability Requirements, Quality Gates
Removed sections: Original template placeholder principles
Templates requiring updates: ✅ .specify/templates/plan-template.md - updated
                             ✅ .specify/templates/spec-template.md - updated
                             ✅ .specify/templates/tasks-template.md - updated
                             ⚠️  .specify/templates/commands/*.md - pending manual review
Follow-up TODOs: [RATIFICATION_DATE]: Original adoption date unknown
-->
# Hackathon II Phase II Todo Full-Stack Web Application Constitution

## Phase 2 Objectives

Phase 2 MUST:

- Deliver **one fully functional, demonstrable user flow**
- Establish **frontend ↔ backend contracts**
- Define **state ownership and lifecycle**
- Validate **Dapr-based service invocation and pub/sub**
- Prove **spec-driven execution discipline**

Phase 2 is about **correctness, traceability, and structure**, not feature quantity.

## Core Principles

### Phase 2 Architecture Non-Negotiables
Kubernetes is the execution environment; Dapr sidecar pattern is mandatory for all services; Infrastructure access is abstracted via Dapr components; Event-driven communication is preferred over synchronous coupling; Spec-Driven Development lifecycle is mandatory (Specify → Plan → Tasks → Implement).

### Service Boundary Rules
Frontend (Next.js) acts as a pure client with no business logic, communicating only via Dapr service invocation and defined backend APIs, handling UI rendering, user interaction, and API request orchestration. Backend (FastAPI + MCP) acts as the orchestration layer owning business rules, state transitions, and workflow coordination, remaining stateless at runtime with state persisted only via Dapr State APIs, exposing versioned HTTP APIs with explicit request/response schemas. Notification Service consumes events via Dapr Pub/Sub, performing asynchronous processing and side-effect operations, but must NOT be invoked synchronously by the frontend or own business-critical state.

### Communication Rules
Allowed communication patterns: Frontend → Backend via Dapr service invocation (HTTP); Backend → Notification Service via Dapr Pub/Sub events. Forbidden communication patterns: Direct service-to-service HTTP without Dapr; Direct Kafka, database, or cache SDK usage; Hardcoded service URLs or ports.

### State Management Rules
Each state store has a single owning service; State access must use Dapr State APIs only; Cross-service state reads or writes are forbidden; State mutations must be explicit, idempotent where applicable, and traceable via logs/events.

### API Design Rules
All APIs in Phase 2 MUST be explicitly versioned and define request schema, response schema, and error contract. APIs must support idempotency where retries are possible and clear error semantics, and be documented in sp.plan.

### Security Constraints
No secrets in code or environment variables; All secrets MUST be accessed via Dapr secret stores; Credentials and API keys are environment-specific and never hardcoded; Internal service calls rely on Dapr identity and service discovery.

## Observability Requirements

Every Phase 2 operation MUST emit structured logs, include trace or correlation identifiers, and be observable across service boundaries. Operations must log state transitions, event publications, and error conditions. Silent failures are forbidden.

## Quality Gates

Phase 2 is considered valid ONLY if:
- Every implemented feature maps to sp.specify
- Every architectural decision maps to sp.plan
- Every code change references a Task ID
- Every user interaction triggers a backend capability
- Every async operation produces an observable event

No task = No code.

## Explicitly Forbidden

Agents and humans MUST NOT:
- Implement features without acceptance criteria
- Bypass the Spec-Kit lifecycle
- Access infrastructure directly
- Introduce speculative or future-phase features
- Modify Phase 1 architecture decisions

If ambiguous requirements are encountered, consult the specification or request clarification before proceeding.

## Governance

This constitution governs how agents and humans are allowed to design, plan, and implement Phase 2. All architectural decisions must align with these principles. Changes to this constitution require explicit approval and documentation of the rationale. The constitution supersedes all other development practices and serves as the ultimate authority for architectural decisions during Phase 2 implementation.

**Version**: 2.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2026-01-08