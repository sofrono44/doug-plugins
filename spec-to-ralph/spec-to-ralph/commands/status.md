---
description: Check if your project is ready for spec-to-ralph conversion. Validates Spec Kit structure, lists available features, and reports any issues.
arguments:
  - name: feature
    description: "Check specific feature(s) only: single ID/name or comma-separated list"
    required: false
---

# /spec-to-ralph:status

Check your project's readiness for Ralph conversion.

## What This Checks

### Project Structure
- [ ] `.specify/` directory exists
- [ ] Flat structure OR feature-based structure detected

### For Flat Structure
- [ ] `.specify/tasks.md` exists and has tasks
- [ ] `.specify/constitution.md` exists (recommended)
- [ ] `.specify/spec.md` exists (recommended)
- [ ] `.specify/plan.md` exists (recommended)

### For Feature Structure
- [ ] `.specify/constitution.md` exists (global rules)
- [ ] `.specify/features/` directory exists
- [ ] Each feature has `tasks.md` (required)
- [ ] Each feature has `spec.md` (recommended)
- [ ] Each feature has `plan.md` (recommended)

### Task Quality (per feature)
- [ ] Tasks use checkbox format (`- [ ]`)
- [ ] Tasks have clear completion criteria
- [ ] Tasks are atomic (not too large)

### Tech Stack Detection
- [ ] Test command identifiable
- [ ] Lint command identifiable
- [ ] Build command identifiable (if applicable)

## Process

### Step 1: Detect Structure

Check for `.specify/` directory:

```
Flat structure:     .specify/tasks.md exists
Feature structure:  .specify/features/ exists
```

Report detected structure type.

### Step 2: List Features (if feature-based)

Scan `.specify/features/` and list all features:

```
📁 Features Detected
====================
001-user-auth       8 tasks (5 incomplete)
002-payment-flow   12 tasks (12 incomplete)  
003-dashboard       6 tasks (0 incomplete) ✓ COMPLETE
004-notifications   4 tasks (4 incomplete)

Total: 4 features, 30 tasks, 21 incomplete
```

### Step 3: Analyze Tasks (per feature or global)

Parse tasks and report:

```
📋 Task Analysis: 001-user-auth
===============================
Total tasks: 8
Incomplete: 5
Complete: 3

Task size assessment:
✅ Good size: 4 tasks
⚠️ Possibly too large: 1 task
   "Implement OAuth with Google, Facebook, and Apple"
```

Flag potentially problematic tasks:
- Tasks with multiple "and" conjunctions
- Tasks without verifiable completion criteria
- Tasks spanning multiple features

### Step 4: Tech Stack Detection

Report detected stack and commands:

```
🔧 Tech Stack
=============
Detected: Node.js / TypeScript
Source: .specify/constitution.md

Backpressure commands:
  ✅ Test: npm test
  ✅ Lint: npm run lint  
  ✅ Build: npm run build
```

### Step 5: Readiness Score

Calculate overall and per-feature readiness:

```
🚦 Overall Readiness: READY (8/10)
===================================

Feature Readiness:
  001-user-auth      ✅ Ready (9/10) - 5 tasks remaining
  002-payment-flow   ✅ Ready (8/10) - 12 tasks remaining  
  003-dashboard      ✓  Complete - skip
  004-notifications  ⚠️ Needs work (5/10) - missing plan.md

Global:
  ✅ constitution.md found
  ✅ Tech stack detected
  ✅ Test commands available
  ⚠️ 1 feature missing plan.md
```

### Step 6: Recommendations

Based on analysis, suggest next steps:

**If Ready:**
```
Ready to run! Suggested commands:

  All features:
  /spec-to-ralph:start --feature all

  Single feature:
  /spec-to-ralph:start --feature 001

  Incomplete features only:
  /spec-to-ralph:start --feature 001,002,004
```

**If Needs Work:**
```
Before proceeding:
1. Add plan.md to feature 004-notifications
2. Split large task in 001-user-auth:
   "Implement OAuth..." → separate tasks per provider
3. Add test commands to constitution.md
```

## Example Output

```
/spec-to-ralph:status

📁 Project Structure: Feature-based
====================================
Location: .specify/features/

📋 Features
===========
  001-user-auth       5/8 tasks incomplete
  002-payment-flow   12/12 tasks incomplete
  003-dashboard       0/6 tasks incomplete ✓
  004-notifications   4/4 tasks incomplete

📊 Summary: 21 tasks remaining across 3 active features

🔧 Tech Stack: Node.js / TypeScript
===================================
  Test:  npm test
  Lint:  npm run lint
  Build: npm run build

⚠️ Issues Found
===============
  - 002-payment-flow: Task may be too large:
    "Implement Stripe checkout with subscriptions and one-time payments"
  - 004-notifications: Missing plan.md (recommended)

🚦 Readiness: READY (7/10)
==========================
Can proceed, but consider addressing issues first.

💡 Suggested Commands
=====================
  All active features:
    /spec-to-ralph:start --feature 001,002,004

  Just auth (start small):
    /spec-to-ralph:start --feature 001

  Preview first:
    /spec-to-ralph:start --feature 001 --dry-run
```
