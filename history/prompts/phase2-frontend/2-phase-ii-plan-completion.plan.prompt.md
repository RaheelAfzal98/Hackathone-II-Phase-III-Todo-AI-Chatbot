---
id: 2
title: Phase II Plan Completion
stage: plan
date: 2026-01-09
surface: agent
model: claude-haiku-4-5-20251001
feature: phase2-frontend
branch: 001-phase2-frontend
user: Hp
command: /sp.plan
labels: [phase-ii, full-stack, plan, completion]
links:
  spec: specs/001-phase2-frontend/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-phase2-frontend/plan.md
 - history/prompts/phase2-frontend/1-phase-ii-full-stack-plan.spec.prompt.md
tests:
 - specs/001-phase2-frontend/tasks.md
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

Complete Phase II implementation plan created with all 10 required sections, covering frontend, backend, authentication, database, and UI/UX requirements for transforming the console-based Todo app into a modern, multi-user, full-stack web application with Neon PostgreSQL, Better Auth (JWT), FastAPI, and Next.js App Router.

## Outcome

- ✅ Impact: Comprehensive plan created covering all Phase II requirements
- 🧪 Tests: Verification checklist included for all requirements
- 📁 Files: Plan document created at specs/001-phase2-frontend/plan.md
- 🔁 Next prompts: Ready for task breakdown and implementation
- 🧠 Reflection: Plan addresses all required technology stack components

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation based on plan