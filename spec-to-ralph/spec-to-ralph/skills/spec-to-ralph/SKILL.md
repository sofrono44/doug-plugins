---
name: spec-to-ralph
description: Knowledge for converting GitHub Spec Kit projects into Ralph Wiggum autonomous loops. Use when generating PROMPT.md files from spec/constitution/plan/tasks, sizing tasks for Ralph, writing backpressure commands, or creating completion promises. Supports both flat and feature-based Spec Kit structures. Provides prompt patterns, task sizing heuristics, and tech stack detection.
---

# Spec-to-Ralph Skill

Reference knowledge for bridging Spec Kit to Ralph Wiggum.

## Spec Kit Structures

### Flat Structure (simple projects)
```
.specify/
├── constitution.md
├── spec.md
├── plan.md
└── tasks.md
```

### Feature-Based Structure (recommended)
```
.specify/
├── constitution.md          # Global rules for all features
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

### Feature Selection

| Selection | Meaning |
|-----------|---------|
| `--feature all` | All features in numerical order |
| `--feature 001` | Match by number prefix |
| `--feature user-auth` | Match by name |
| `--feature 001-user-auth` | Match by full ID |
| `--feature 001,002,003` | Multiple specific features |
| (none) | Auto-detect or prompt |

## Core Concepts

### Ralph Prompt Requirements

Ralph prompts must have:

1. **Context pointing to state files** - Ralph reads specs, not memory
2. **Explicit process steps** - Numbered, repeatable per iteration
3. **Backpressure commands** - Tests/lint that MUST pass
4. **Completion promises** - Exact string matching with `<promise>` tags
5. **Escape hatches** - What to do when stuck

### Spec Kit → Ralph Mapping

| Spec Kit Artifact | Ralph Usage |
|-------------------|-------------|
| constitution.md | Constraints section (non-negotiable rules) |
| spec.md | Context section (what we're building) |
| plan.md | Context + backpressure commands |
| tasks.md | The work queue Ralph iterates through |

## Task Sizing

### Good Ralph Task Size
- Completable in 1-3 iterations
- Single logical change
- Clear pass/fail test
- One commit per task

### Iteration Budgets

| Task Type | Iterations | Notes |
|-----------|------------|-------|
| Bug fix (known) | 1-2 | Clear target |
| Bug fix (unknown) | 3-5 | Needs exploration |
| New endpoint | 2-3 | Mechanical |
| UI component | 2-4 | May need iteration |
| Single-file refactor | 2-3 | Predictable |
| Multi-file refactor | 5-10 | Complex |
| Test coverage | 1-2 per test | Fast |

### Splitting Large Tasks

**Vertical slicing** (by feature layer):
```
"Add user profile" →
1. Create profile model
2. Add GET endpoint
3. Add PUT endpoint
4. Create UI component
5. Connect to API
```

**Horizontal slicing** (by concern):
```
"Add validation" →
1. Add email validation
2. Add phone validation
3. Add address validation
```

## Tech Stack Detection

### Node.js / TypeScript
Triggers: `typescript`, `node`, `npm`, `react`, `next.js`
```bash
npm test
npm run lint
npm run build
```

### Python
Triggers: `python`, `django`, `flask`, `fastapi`, `pytest`
```bash
pytest
ruff check .
mypy .  # if mentioned
```

### Rust
Triggers: `rust`, `cargo`
```bash
cargo test
cargo clippy
cargo build
```

### Go
Triggers: `golang`, `go mod`, `go test`
```bash
go test ./...
go vet ./...
go build ./...
```

## Prompt Template

```markdown
# Ralph Loop: [Project Name]

## Context
Read these files before starting:
- `@.specify/constitution.md` - Non-negotiable rules
- `@.specify/spec.md` - What we're building
- `@.specify/plan.md` - How we're building it

## Your Mission
Complete all tasks in `.specify/tasks.md` systematically.

## Process (Every Iteration)

1. **Read Tasks**: Find next `- [ ]` unchecked task
2. **Search First**: Use grep/find to understand existing code
3. **Implement**: Make minimal changes for the task
4. **Verify**: Run ALL feedback loops:
   ```bash
   [TEST_COMMAND]
   [LINT_COMMAND]
   [BUILD_COMMAND]
   ```
5. **Mark Complete**: Change `- [ ]` to `- [x]`
6. **Commit**: `git add -A && git commit -m "feat: [task]"`
7. **Continue**: Move to next task

## Constraints
[EXTRACTED_FROM_CONSTITUTION]

## Completion Signals

All tasks done + tests pass:
<promise>ALL_TASKS_COMPLETE</promise>

Unable to progress after 10 iterations:
<promise>BLOCKED</promise>

## If Stuck

After 5 attempts on one task:
1. Add `BLOCKED:` prefix to task
2. Document issue in task description
3. Move to next task
4. Continue working

After 3+ blocked tasks:
1. Create BLOCKED.md with details
2. Output: <promise>PARTIALLY_BLOCKED</promise>
```

## Completion Promise Patterns

Always use exact strings in `<promise>` tags:

| Outcome | Promise |
|---------|---------|
| All done | `<promise>ALL_TASKS_COMPLETE</promise>` |
| Stuck | `<promise>BLOCKED</promise>` |
| Partial | `<promise>PARTIALLY_BLOCKED</promise>` |
| Phase done | `<promise>PHASE1_DONE</promise>` |

**Note**: `--completion-promise` uses exact string matching. Can't have multiple conditions. Use `--max-iterations` as primary safety.

## Common Patterns

### TDD Loop
```markdown
1. Write failing test for task's acceptance criteria
2. Run tests - confirm new test fails
3. Implement minimum code to pass
4. Run ALL tests - confirm all pass
5. Refactor if needed (tests must stay green)
6. Mark complete, commit
```

### Migration Loop
```markdown
1. Pick ONE item from migration checklist
2. Make the change
3. Run full test suite
4. If fail: revert and try different approach
5. If pass: commit and update checklist
```

### Bug Hunt Loop
```markdown
1. First iteration: reproduce bug, write failing test
2. Search codebase for related code
3. Form hypothesis, implement fix
4. Run failing test - must pass
5. Run full suite - no regressions
6. Document fix in commit
```

## Anti-Patterns

❌ **Vague instructions**: "Make the code better"
❌ **No backpressure**: No test/lint verification
❌ **Unbounded scope**: "Keep improving until perfect"
❌ **Human judgment**: "Make the UI look good"
❌ **Multiple completion conditions**: Use iterations instead

## Iteration Calculation

```python
def calculate_iterations(task_count, buffer=0.2):
    base = task_count * 4
    with_buffer = int(base * (1 + buffer))
    return min(max(with_buffer, 10), 50)
```

First run: Cap at 50 for cost control
Subsequent runs: Increase based on task complexity
