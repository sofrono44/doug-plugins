---
description: Generate a Ralph Wiggum prompt from your GitHub Spec Kit project. Analyzes constitution, spec, plan, and tasks to create an optimized autonomous loop prompt. Supports feature selection for multi-feature Spec Kit projects.
arguments:
  - name: feature
    description: "Feature(s) to include: 'all', single feature ID/name (e.g., '001' or 'user-auth'), or comma-separated list (e.g., '001,002,003')"
    required: false
  - name: max-iterations
    description: "Override auto-calculated max iterations"
    required: false
---

# /spec-to-ralph:generate

Generate an optimized Ralph Wiggum prompt from your Spec Kit project.

## Prerequisites

This command supports two Spec Kit structures:

### Flat Structure (simple projects)
```
.specify/
├── constitution.md
├── spec.md
├── plan.md
└── tasks.md
```

### Feature-Based Structure (recommended for larger projects)
```
.specify/
├── constitution.md
└── features/
    ├── 001-user-auth/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 002-payment-flow/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    └── 003-dashboard/
        ├── spec.md
        ├── plan.md
        └── tasks.md
```

## Feature Selection

### All Features
```
/spec-to-ralph:generate --feature all
```
Generates a prompt that works through all features sequentially.

### Single Feature
```
/spec-to-ralph:generate --feature 001
/spec-to-ralph:generate --feature user-auth
/spec-to-ralph:generate --feature 001-user-auth
```
Any of these formats work - matches by number prefix or name.

### Multiple Features
```
/spec-to-ralph:generate --feature 001,002,003
/spec-to-ralph:generate --feature user-auth,payment-flow
```
Comma-separated list, processed in the order specified.

### Auto-Detection
```
/spec-to-ralph:generate
```
- If flat structure: uses root spec/plan/tasks
- If feature structure with one feature: uses that feature
- If feature structure with multiple: prompts for selection

## What This Command Does

1. **Validates** your Spec Kit project structure
2. **Extracts** constraints from constitution.md
3. **Detects** your tech stack and appropriate test/lint commands
4. **Counts** tasks and calculates optimal iteration budget
5. **Generates** `PROMPT.md` optimized for Ralph convergence
6. **Generates** `ralph-config.md` with the recommended command

## Process

### Step 1: Detect Project Structure

Check for Spec Kit layout:

**Flat structure** (if `.specify/tasks.md` exists):
```
.specify/
├── constitution.md
├── spec.md
├── plan.md
└── tasks.md
```

**Feature structure** (if `.specify/features/` exists):
```
.specify/
├── constitution.md
└── features/
    ├── 001-user-auth/
    ├── 002-payment-flow/
    └── 003-dashboard/
```

### Step 2: Resolve Feature Selection

If `--feature` argument provided:
- `all` → Include all features in order (001, 002, 003...)
- Single value → Match by prefix (`001`) or name (`user-auth`) or full (`001-user-auth`)
- Comma-separated → Parse and validate each, maintain specified order

If no `--feature` argument:
- Flat structure → Use root spec files
- Single feature → Use that feature automatically
- Multiple features → List available and ask user to select

### Step 3: Load Feature Files

For each selected feature, load:
- `features/NNN-name/spec.md`
- `features/NNN-name/plan.md`
- `features/NNN-name/tasks.md`

Always load root `constitution.md` (applies to all features).

### Step 4: Analyze Content

Read each file and extract:

**From constitution.md (global):**
- Non-negotiable rules (bullet points, numbered lists)
- Tech stack requirements
- Testing requirements
- Coding standards

**From each feature's plan.md:**
- Architecture decisions
- Dependencies
- Build/test commands

**From each feature's tasks.md:**
- Count of incomplete tasks (`- [ ]` checkboxes)
- Task descriptions for complexity estimation

### Step 5: Detect Tech Stack

Based on constitution and plan content, identify:

| Stack | Test Command | Lint Command | Build Command |
|-------|--------------|--------------|---------------|
| Node/TS | `npm test` | `npm run lint` | `npm run build` |
| Python | `pytest` | `ruff check .` | - |
| Rust | `cargo test` | `cargo clippy` | `cargo build` |
| Go | `go test ./...` | `go vet ./...` | `go build ./...` |

If commands are explicitly mentioned in constitution/plan, prefer those.

### Step 6: Calculate Iterations

```
total_tasks = sum of incomplete tasks across all selected features
base_iterations = total_tasks × 4
with_buffer = base_iterations × 1.2
max_iterations = min(with_buffer, 50)  # Cap for cost control
```

For multi-feature runs, add 5 iterations per feature transition.

### Step 7: Generate PROMPT.md

For **single feature**, generate focused prompt:
```markdown
# Ralph Loop: [Project] - Feature [NNN-name]

## Context
- `@.specify/constitution.md` - Global rules
- `@.specify/features/NNN-name/spec.md` - This feature's spec
- `@.specify/features/NNN-name/plan.md` - This feature's plan

## Your Mission
Complete all tasks in `.specify/features/NNN-name/tasks.md`
```

For **multiple features**, generate sequential prompt:
```markdown
# Ralph Loop: [Project] - Features [list]

## Context
- `@.specify/constitution.md` - Global rules
- Feature specs in `.specify/features/`

## Your Mission
Complete features in this order:
1. 001-user-auth (8 tasks)
2. 002-payment-flow (12 tasks)
3. 003-dashboard (6 tasks)

## Process
Work through each feature completely before moving to the next.
For each feature:
1. Read its spec.md and plan.md
2. Complete all tasks in its tasks.md
3. When all tasks marked [x], move to next feature
```

### Step 8: Generate ralph-config.md

Create a config file with:
- Recommended `/ralph-loop` command
- Features included and task counts
- Rationale for iteration count
- Pre-run checklist
- Monitoring tips
- Recovery commands

### Step 9: Report Results

Output:
- Files generated
- Features included
- Total task count
- Recommended iterations
- Next step command

## Example Usage

Basic (auto-detect):
```
/spec-to-ralph:generate
```

All features:
```
/spec-to-ralph:generate --feature all
```

Single feature:
```
/spec-to-ralph:generate --feature 001
/spec-to-ralph:generate --feature user-auth
```

Multiple specific features:
```
/spec-to-ralph:generate --feature 001,003
/spec-to-ralph:generate --feature user-auth,dashboard
```

With iteration override:
```
/spec-to-ralph:generate --feature all --max-iterations 100
```

## Output

After running, you'll have:

```
project/
├── PROMPT.md           # Ralph-optimized prompt
├── ralph-config.md     # Recommended settings
└── .specify/
    ├── constitution.md
    └── features/
        ├── 001-user-auth/
        ├── 002-payment-flow/
        └── 003-dashboard/
```

## Next Steps

After generation, run:

```
/ralph-loop "Follow PROMPT.md to complete all tasks" --max-iterations [N] --completion-promise "ALL_TASKS_COMPLETE"
```

Or use `/spec-to-ralph:start` to generate AND start Ralph in one command.
