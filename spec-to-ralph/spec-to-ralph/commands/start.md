---
description: Generate a Ralph prompt from Spec Kit AND immediately start the autonomous loop. One command to go from specs to working code. Supports feature selection for multi-feature projects.
arguments:
  - name: feature
    description: "Feature(s) to include: 'all', single feature ID/name (e.g., '001' or 'user-auth'), or comma-separated list (e.g., '001,002,003')"
    required: false
  - name: max-iterations
    description: "Override auto-calculated max iterations (default: auto)"
    required: false
  - name: dry-run
    description: "Generate prompt but don't start Ralph (preview mode)"
    required: false
---

# /spec-to-ralph:start

Generate a Ralph prompt from your Spec Kit project and immediately start the autonomous loop.

## What This Does

1. Runs `/spec-to-ralph:generate` to create PROMPT.md
2. Creates a git checkpoint for safety
3. Starts Ralph with the generated prompt

This is the "one command to rule them all" for spec-driven autonomous development.

## Feature Selection

### All Features
```
/spec-to-ralph:start --feature all
```
Runs through every feature in your `.specify/features/` directory sequentially.

### Single Feature
```
/spec-to-ralph:start --feature 001
/spec-to-ralph:start --feature user-auth
/spec-to-ralph:start --feature 001-user-auth
```
Focus Ralph on just one feature. Matches by number prefix, name, or full directory name.

### Multiple Specific Features
```
/spec-to-ralph:start --feature 001,002
/spec-to-ralph:start --feature user-auth,payment-flow
```
Run specific features in the order you specify. Useful for:
- Dependent features that must be done in order
- Skipping features that are already complete
- Testing a subset before running all

### Auto-Detection
```
/spec-to-ralph:start
```
- Flat structure → uses root spec files
- One feature → uses that feature  
- Multiple features → lists available and prompts for selection

## Prerequisites

- Spec Kit project with either:
  - Flat: `.specify/tasks.md` (minimum)
  - Features: `.specify/features/*/tasks.md`
- Ralph Wiggum plugin installed (`/plugin install ralph-wiggum@claude-plugins-official`)
- Clean git working directory (recommended)

## Process

### Step 1: Generate Prompt

Execute the full `/spec-to-ralph:generate` workflow with feature selection:
- Detect project structure (flat vs features)
- Resolve feature selection from `--feature` argument
- Validate selected features exist
- Extract constraints and tech stack
- Generate PROMPT.md and ralph-config.md

### Step 2: Safety Checkpoint

Before starting Ralph:

```bash
git add -A
git commit -m "checkpoint: pre-ralph state" --allow-empty
```

This creates a restore point if Ralph goes sideways.

### Step 3: Display Summary

Show the user:
- Number of tasks to complete
- Max iterations configured
- Backpressure commands that will run
- Estimated cost range (rough)

### Step 4: Start Ralph

Execute:

```
/ralph-loop "Follow PROMPT.md to complete all tasks in .specify/tasks.md. Read the spec files first, then work through tasks systematically." --max-iterations [CALCULATED] --completion-promise "ALL_TASKS_COMPLETE"
```

## Dry Run Mode

Use `--dry-run` to preview without starting:

```
/spec-to-ralph:start --dry-run
```

This will:
- Generate PROMPT.md
- Show the Ralph command that WOULD run
- NOT actually start the loop

Useful for reviewing the generated prompt before committing to an autonomous run.

## Example Usage

Basic (auto-detect structure and features):
```
/spec-to-ralph:start
```

All features:
```
/spec-to-ralph:start --feature all
```

Single feature:
```
/spec-to-ralph:start --feature 001
/spec-to-ralph:start --feature user-auth
```

Multiple specific features:
```
/spec-to-ralph:start --feature 001,002,003
/spec-to-ralph:start --feature user-auth,payment-flow,dashboard
```

With iteration override:
```
/spec-to-ralph:start --feature all --max-iterations 100
```

Preview mode (generate but don't run):
```
/spec-to-ralph:start --feature 001 --dry-run
```

## Safety Notes

**Before running:**
- Review your `.specify/tasks.md` for well-defined tasks
- Ensure test commands work manually
- Consider running in a VM or container for isolation

**During the loop:**
- Monitor token usage
- Watch for repeated errors (sign of stuck loop)
- Use `Ctrl+C` or `/cancel-ralph` to stop if needed

**After the loop:**
- Review git diff before pushing
- Run tests manually to verify
- Check BLOCKED.md if created

## Recovery

If Ralph gets stuck or produces bad output:

```bash
# Stop the loop
/cancel-ralph

# Review what changed
git diff

# Revert if needed
git reset --hard HEAD~1

# Or revert to checkpoint
git log --oneline  # Find checkpoint commit
git reset --hard <checkpoint-sha>
```

## Cost Estimation

Rough estimates based on task count:

| Tasks | Iterations | Est. Cost (Opus) | Est. Cost (Sonnet) |
|-------|------------|------------------|-------------------|
| 5     | 20-25      | $5-15           | $1-3              |
| 10    | 40-50      | $15-40          | $3-8              |
| 20    | 50+ (capped)| $30-80         | $6-15             |

These are rough estimates. Actual costs vary based on:
- Context size (codebase)
- Task complexity
- Number of retries needed

## What Success Looks Like

When Ralph completes successfully:

1. All tasks in `.specify/tasks.md` marked `[x]`
2. Each task has a corresponding git commit
3. All backpressure checks pass
4. Output contains `<promise>ALL_TASKS_COMPLETE</promise>`

You'll wake up to:
- Working code implementing your spec
- Clean git history showing progress
- Tests passing
