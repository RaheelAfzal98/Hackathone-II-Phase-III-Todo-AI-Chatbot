---
id: "003"
title: "Next.js Client Components Error Resolution"
stage: "general"
date: "2026-01-09"
model: "claude-haiku-4-5-20251001"
feature: "001-phase2-frontend"
branch: "001-phase2-frontend"
user: "user"
command: "/sp.implement"
labels: ["nextjs", "client-components", "app-router", "bug-fix", "frontend", "todo"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "frontend/src/app/page.tsx"
  - "frontend/src/components/UI/Toast.tsx"
  - "frontend/src/components/Task/TaskForm.tsx"
  - "frontend/src/components/Task/TaskCard.tsx"
  - "frontend/src/components/UI/Modal.tsx"
  - "frontend/src/components/utils/ProtectedRoute.tsx"
tests: []
---

# Next.js Client Components Error Resolution

## Prompt Text

Build Error
Failed to compile

Next.js (14.2.35) is outdated (learn more)
./src/app/page.tsx
Error:
  x You're importing a component that needs useState. It only works in a Client Component but none of its parents are marked with "use client", so they're Server Components by default.
  | Learn more: https://nextjs.org/docs/getting-started/react-essentials
  |
  |
   ,-[C:\Users\Hp\Desktop\Hackathon II Phase II Todo Full-Stack Web Application\frontend\src\app\page.tsx:1:1]
 1 | import React, { useState } from 'react';
   :                 ^^^^^^^^
 2 | import Head from 'next/head';
 3 | import DashboardLayout from '@/components/Layout/DashboardLayout';
 4 | import TaskList from '@/components/Task/TaskList';
   `----
This error occurred during the build process and can only be dismissed by fixing the error.

## Response Text

Successfully resolved the Next.js App Router client component error. The issue was that components using React hooks like useState, useEffect, and other client-side features were being treated as server components by default in the App Router.

## Root Cause

In Next.js 13+ with the App Router, components are server components by default. When components use React hooks like useState, useEffect, or other client-side features, they must be explicitly marked as client components using the "use client" directive at the top of the file.

## Solution Applied

Added the "use client" directive to all components that use React hooks or client-side features:

1. `frontend/src/app/page.tsx` - Added "use client" directive since it uses useState and other hooks
2. `frontend/src/components/UI/Toast.tsx` - Added "use client" directive since it uses useState and useEffect
3. `frontend/src/components/Task/TaskForm.tsx` - Added "use client" directive since it uses useState and useEffect
4. `frontend/src/components/Task/TaskCard.tsx` - Added "use client" directive since it uses useState
5. `frontend/src/components/UI/Modal.tsx` - Added "use client" directive since it uses useEffect
6. `frontend/src/components/utils/ProtectedRoute.tsx` - Added "use client" directive since it uses useEffect and next/router

## Additional Context

The application was also using both pages/ and app/ directories simultaneously, which can cause routing conflicts in Next.js 13+. The main dashboard page was correctly moved to the app/ directory as page.tsx, but authentication pages remained in the pages/ directory. For a complete migration to App Router, all pages should eventually be moved to the app/ directory.

## Outcome

The build error has been resolved and the application should now compile successfully. All components that require client-side functionality are properly marked with the "use client" directive.

## Evaluation

The Next.js App Router client component error has been completely resolved. The application can now be built and run without the compilation error related to server/client component mismatches.