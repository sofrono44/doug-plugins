# spec-to-ralph

Bridge GitHub Spec Kit projects to Ralph Wiggum autonomous loops.

## What This Does

Takes your spec-driven development artifacts and generates optimized prompts for autonomous AI coding:

```
Spec Kit (.specify/)                    →  Ralph Wiggum Loop
├── constitution.md                          ├── PROMPT.md (optimized)
└── features/                                ├── ralph-config.md  
    ├── 001-user-auth/                       └── /ralph-loop command
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 002-payment-flow/
    └── 003-dashboard/
```

## Installation

```bash
# Add the marketplace (if not already added)
/plugin marketplace add switchfin/spec-to-ralph

# Install the plugin
/plugin install spec-to-ralph
```

**Dependency**: Requires the `ralph-wiggum` plugin:
```bash
/plugin install ralph-wiggum@claude-plugins-official
```

## Commands

### `/spec-to-ralph:status`

Check if your project is ready for conversion:

```
/spec-to-ralph:status
```

Shows:
- Project structure (flat vs feature-based)
- Available features with task counts
- Tech stack detection
- Readiness score

### `/spec-to-ralph:generate`

Generate Ralph prompt files without starting the loop:

```bash
# All features
/spec-to-ralph:generate --feature all

# Single feature
/spec-to-ralph:generate --feature 001
/spec-to-ralph:generate --feature user-auth

# Multiple specific features
/spec-to-ralph:generate --feature 001,002,003
```

### `/spec-to-ralph:start`

Generate AND immediately start Ralph:

```bash
# All features
/spec-to-ralph:start --feature all

# Single feature (good for testing)
/spec-to-ralph:start --feature 001

# Multiple features
/spec-to-ralph:start --feature user-auth,payment-flow

# Preview without starting
/spec-to-ralph:start --feature 001 --dry-run
```

## Feature Selection

| Option | What it does |
|--------|--------------|
| `--feature all` | Run all features in order (001, 002, 003...) |
| `--feature 001` | Match by number prefix |
| `--feature user-auth` | Match by name |
| `--feature 001-user-auth` | Match by full directory name |
| `--feature 001,002` | Comma-separated list, in specified order |
| (no flag) | Auto-detect or prompt for selection |

## Example Workflow

```bash
# 1. Set up your project with Spec Kit
uvx --from git+https://github.com/github/spec-kit.git specify init my-project

# 2. Define your specs (Spec Kit creates feature-based structure)
#    - Edit .specify/constitution.md (global rules)
#    - Edit .specify/features/001-feature-name/spec.md
#    - Edit .specify/features/001-feature-name/plan.md
#    - Edit .specify/features/001-feature-name/tasks.md

# 3. Check readiness
/spec-to-ralph:status

# 4. Start with one feature to test
/spec-to-ralph:start --feature 001 --dry-run   # Preview
/spec-to-ralph:start --feature 001             # Run

# 5. Once confident, run all features
/spec-to-ralph:start --feature all

# 6. Wake up to working code
```

## What Makes a Good Spec Kit Project for Ralph

### Tasks (`tasks.md`)

✅ Good tasks:
```markdown
- [ ] Add email validation to signup form
- [ ] Create GET /api/users endpoint
- [ ] Write unit tests for auth middleware
```

❌ Bad tasks:
```markdown
- [ ] Build the entire authentication system
- [ ] Make everything work better
- [ ] Fix all the bugs
```

### Constitution (`constitution.md`)

Include:
- Tech stack requirements
- Testing requirements (e.g., "all code must have tests")
- Coding standards
- Non-negotiable rules

### Plan (`plan.md`)

Include:
- Architecture decisions
- Explicit test/lint/build commands
- Dependencies and their purpose

## How It Works

1. **Parses** your Spec Kit artifacts
2. **Extracts** constraints from constitution.md
3. **Detects** your tech stack (Node, Python, Rust, Go)
4. **Calculates** optimal iteration budget
5. **Generates** a prompt with:
   - Context pointing to spec files
   - Explicit process steps
   - Backpressure commands (tests/lint)
   - Completion promises
   - Escape hatches for when stuck

## Configuration

Override auto-calculated iterations:
```
/spec-to-ralph:start --max-iterations 30
```

## Safety

- Always creates a git checkpoint before starting
- Caps iterations at 50 for first run (cost control)
- Generates escape hatch instructions
- Provides recovery commands

## License

MIT
