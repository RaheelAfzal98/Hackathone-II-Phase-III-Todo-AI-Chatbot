---
id: 3
title: Phase II Frontend Plan Completion
stage: plan
date: 2026-01-09
surface: agent
model: claude-haiku-4-5-20251001
feature: phase2-frontend
branch: 001-phase2-frontend
user: Hp
command: /sp.plan
labels: [phase-ii, frontend, plan, completion]
links:
  spec: specs/001-phase2-frontend/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-phase2-frontend/plan.md
 - specs/001-phase2-frontend/research.md
 - specs/001-phase2-frontend/data-model.md
 - specs/001-phase2-frontend/quickstart.md
 - specs/001-phase2-frontend/contracts/task-api-contract.md
tests:
 - specs/001-phase2-frontend/tasks.md
---

## Prompt

```text
Frontend Only (Phase II: Todo Full-Stack Web Application)

You are executing **Phase II (Web Application)** using **Spec-Driven Development (SDD)** with **Claude Code + Spec-Kit Plus**.

This document defines **HOW the FRONTEND will be executed**, strictly aligned with the approved **sp.specify (frontend)**.
Nothing may be added, skipped, or assumed.

---

## 1. PLAN OBJECTIVE

Transform the Phase I console todo app into a **modern, secure, multi-user web frontend** that:

- Is fully authenticated using **Better Auth + JWT**
- Communicates securely with FastAPI REST APIs
- Displays **only user-owned data**
- Implements **all 5 Basic Level features**
- Delivers a **professional, beautiful, responsive UI**
- Is **production-ready**, not experimental

---

## 2. EXECUTION CONSTRAINTS (MANDATORY)

- No manual coding outside Claude Code
- No backend logic in frontend
- No scope beyond Phase II (Basic Level)
- Follow:
  - `/frontend/CLAUDE.md`
  - `/specs/features/*`
  - `/specs/api/rest-endpoints.md`
  - `/specs/ui/*`
- Next.js **App Router only**
- Server Components by default

---

## 3. FRONTEND ARCHITECTURE PLAN

### 3.1 Folder & Routing Strategy
- `/app`
  - `/login`
  - `/signup`
  - `/tasks` (protected)
  - `layout.tsx` (auth-aware root layout)
- `/components`
  - UI primitives (Button, Input, Modal, Loader)
  - Task components (TaskCard, TaskList, TaskForm)
- `/lib`
  - `api.ts` (central API client)
  - `auth.ts` (Better Auth helpers)
- `/styles`
  - Tailwind configuration only

---

## 4. AUTHENTICATION IMPLEMENTATION PLAN

### 4.1 Better Auth Setup
- Enable **JWT plugin**
- Configure shared secret via `BETTER_AUTH_SECRET`
- Ensure session persistence across reloads

### 4.2 Auth Flow Execution
1. User visits protected route
2. Frontend checks auth session
3. If unauthenticated → redirect to `/login`
4. If authenticated → allow access

### 4.3 Login / Signup UI
- Controlled forms
- Inline validation
- Loading states on submit
- Friendly error messaging
- Auto-redirect on success

### 4.4 Logout Flow
- Clear session
- Clear cached state
- Redirect to login screen

---

## 5. JWT & API COMMUNICATION PLAN

### 5.1 Central API Client
- All API calls routed through `/lib/api.ts`
- Automatically attach:
Authorization: Bearer <JWT>

yaml
Copy code
- No direct `fetch` usage elsewhere

### 5.2 Unauthorized Handling
- Global handling for `401 Unauthorized`
- Force logout and redirect to `/login`
- Clear stale UI state

---

## 6. TASK CRUD EXECUTION PLAN (ALL 5 FEATURES)

### 6.1 Task List (GET)
- Fetch on dashboard load
- Display:
- Title
- Completion status
- Created date
- Empty state messaging
- Loading skeleton

### 6.2 Create Task (POST)
- Modal or inline form
- Required title validation
- Disable submit during request
- Optimistic UI update on success

### 6.3 View Task (GET by ID)
- Inline expansion or detail view
- Read-only fields
- Graceful loading state

### 6.4 Update Task (PUT)
- Editable form
- Pre-filled values
- Save / Cancel actions
- Error rollback handling

### 6.5 Delete Task (DELETE)
- Confirmation modal (mandatory)
- Disabled state during request
- Immediate removal on success

### 6.6 Toggle Completion (PATCH)
- One-click interaction
- Visual feedback
- Optimistic UI update

---

## 7. TASK FILTERING & STATE PLAN

- Filters:
- All
- Pending
- Completed
- Filter state preserved during session
- No backend logic duplication
- Clear empty states per filter

---

## 8. UI / UX EXECUTION PLAN (PROFESSIONAL QUALITY)

### 8.1 Design System Enforcement
- Consistent spacing
- Clear typography hierarchy
- Unified button styles
- Predictable interactions

### 8.2 Interaction Principles
- No hidden actions
- Clear primary CTAs
- Confirm destructive actions
- Smooth transitions

### 8.3 Accessibility Basics
- Keyboard navigation
- Focus states
- Readable contrast

---

## 9. RESPONSIVENESS PLAN

- Desktop-first layout
- Mobile adaptive stacking
- Touch-friendly controls
- No horizontal overflow
- Consistent UX across breakpoints

---

## 10. ERROR, LOADING & FEEDBACK PLAN

- Page-level loaders
- Button-level loaders
- Inline validation messages
- Friendly API error messages
- Non-blocking success feedback

User must **always know system state**.

---

## 11. IMPLEMENTATION ORDER (MILESTONES)

1. Base layout & routing
2. Authentication UI & session handling
3. API client with JWT support
4. Task dashboard UI
5. Task CRUD interactions
6. Filtering & state polish
7. Responsive & UX refinement
8. Final spec compliance review

---

## 12. FINAL QUALITY CHECKLIST (MANDATORY)

Frontend is complete only if:
- JWT is attached to every API request
- Unauthorized access is impossible
- All 5 Basic Level features work
- UI is clean, responsive, and polished
- No broken loading or error states
- Specs and implementation fully match
- Zero missing Phase II requirements

---

## FINAL STATEMENT

This `sp.plan` guarantees a **secure, elegant, production-ready frontend** that fully satisfies **Phase II Basic Level requirements** using **Spec-Kit Plus + Claude Code**, with **no missing items and no amb
```

## Response snapshot

Successfully completed the Phase II frontend planning process, creating all required artifacts:

1. **plan.md**: Comprehensive implementation plan with architecture, structure, and design elements
2. **research.md**: Research summary with technology decisions and patterns
3. **data-model.md**: Complete data models for Task, User Session, and UI State entities
4. **quickstart.md**: Quickstart guide with setup instructions and development workflow
5. **contracts/task-api-contract.md**: Complete API contract defining frontend-backend communication

The plan aligns with the constitution requirements and provides a complete roadmap for implementing the Phase II frontend todo management UI with authentication, task management features, and responsive design.

## Outcome

- ✅ Impact: Complete frontend plan created with all required artifacts
- 🧪 Tests: API contracts defined with proper error handling
- 📁 Files: All planning artifacts created in specs/001-phase2-frontend/
- 🔁 Next prompts: Ready for task breakdown and implementation
- 🧠 Reflection: Plan fully aligned with spec and constitution requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin task breakdown with /sp.tasks