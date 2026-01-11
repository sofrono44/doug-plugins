<!-- Logo/Banner placeholder - replace with your own -->
<div align="center">
  <h1>sofrono-plugins</h1>
  <p><strong>Productivity plugins for Claude Code that supercharge your development workflow</strong></p>

  <a href="https://github.com/sofrono44/sofrono-plugins/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  </a>
  <a href="https://github.com/sofrono44/sofrono-plugins/stargazers">
    <img src="https://img.shields.io/github/stars/sofrono44/sofrono-plugins" alt="Stars">
  </a>
  <a href="https://github.com/sofrono44/sofrono-plugins/issues">
    <img src="https://img.shields.io/github/issues/sofrono44/sofrono-plugins" alt="Issues">
  </a>
</div>

---

## Why sofrono-plugins?

Claude Code is powerful out of the box—but these plugins take it further:

- **Stay compliant** — finra-review-skill catches regulatory issues in broker-dealer marketing materials before they become problems
- **Bridge the gap** — spec-to-ralph is the first plugin connecting GitHub Spec Kit with ralph-wiggum for seamless spec-to-implementation workflows
- **Think better** — Use proven frameworks (SCAMPER, Question Storming) to break through creative blocks
- **Ship faster** — Go from structured specs to autonomous coding in one command
- **Stay in flow** — Everything runs inside Claude Code, no context switching

---

## Quick Start

```bash
# Add the marketplace
claude plugin marketplace add https://github.com/sofrono44/sofrono-plugins

# Install a plugin
claude plugin install spec-to-ralph@sofrono-plugins
```

---

## Plugins

### spec-to-ralph

**The bridge between [GitHub Spec Kit](https://github.com/github/spec-kit) and [ralph-wiggum](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum).**

These two tools are powerful on their own:
- **GitHub Spec Kit** — A structured approach to defining features through constitution, spec, plan, and task files
- **ralph-wiggum** — An autonomous coding loop that executes complex implementations with minimal intervention

**spec-to-ralph** is the first plugin to connect them. It transforms your Spec Kit artifacts into optimized Ralph prompts—so you go from structured planning to autonomous execution in one command.

| Command | Description |
|---------|-------------|
| `/status` | Validate your Spec Kit structure is ready for conversion |
| `/generate` | Create an optimized Ralph prompt from your specs |
| `/start` | Generate the prompt AND launch the autonomous loop immediately |

**Why this matters:**
- No manual prompt crafting—your specs become the prompt
- Ralph gets full context: requirements, constraints, and acceptance criteria
- Supports both flat and feature-based Spec Kit structures

> **Important:** When using spec-to-ralph, skip the `/speckit.implement` step in your Spec Kit workflow. Ralph-wiggum handles the implementation instead—that's the whole point! Your flow becomes: `/speckit.constitution` → `/speckit.spec` → `/speckit.plan` → `/speckit.tasks` → **`/start`** (spec-to-ralph takes over here).

**Example workflow:**

```bash
# 1. You've already written your Spec Kit files
ls spec/
# constitution.md  spec.md  plan.md  tasks.md

# 2. Check readiness
/status
# Spec Kit valid. 4 tasks found. Ready for Ralph.

# 3. Go autonomous
/start
# Generating Ralph prompt...
# Starting autonomous loop for "User Authentication Module"
# Claude is now implementing your spec...
```

**Use case:** You've spent time carefully speccing a feature with Spec Kit. Instead of manually implementing or writing a custom prompt, run `/start` and let Ralph execute your vision autonomously while you review the output.

> **New to these tools?**
> - [GitHub Spec Kit documentation](https://github.com/github/spec-kit)
> - [ralph-wiggum plugin guide](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum)

---

## Skills

### finra-review-skill

**FINRA Rule 2210 compliance review for broker-dealer marketing materials.**

A specialized compliance tool that analyzes marketing content against FINRA communications rules. Identifies potential regulatory issues, provides rule citations, and suggests compliant alternatives.

| Skill | Description |
|-------|-------------|
| `finra-review` | Analyze marketing content for FINRA Rule 2210 compliance |

**What it checks:**
- Promissory language ("guaranteed returns")
- Unbalanced claims (benefits without risks)
- Performance presentation standards
- Testimonial requirements
- Social media compliance (character limits, disclosures)

**Example:**

```
You: Review this for FINRA compliance:
"Achieve consistent, market-beating returns with our AI-driven strategies."

Claude:
Issue 1: Promissory Performance Claims
Original Text: "Achieve consistent, market-beating returns"
Rule Citation: FINRA Rule 2210(d)(1)(B)
Compliance Concern: This language promises guaranteed outcomes.
Suggested Revision: "Our AI-driven strategies seek competitive risk-adjusted
returns. Past performance is not indicative of future results."
Risk Level: High
```

**Use case:** Before publishing marketing materials, social media posts, or client communications, run a preliminary compliance check to identify potential FINRA violations and get suggested compliant rewrites.

**⚠️ Important:** This is a review aid for preliminary compliance screening. Does not replace registered principal review, FINRA filing requirements, or legal counsel.

---

### scamper

**Systematic creativity for product and feature ideation.**

Applies the SCAMPER methodology—a structured approach to innovation used by product teams worldwide.

| Letter | Prompt |
|--------|--------|
| **S** | Substitute — What can be replaced? |
| **C** | Combine — What can be merged? |
| **A** | Adapt — What can be adjusted for a new use? |
| **M** | Modify — What can be changed (bigger, smaller, different)? |
| **P** | Put to other uses — What else could this be used for? |
| **E** | Eliminate — What can be removed? |
| **R** | Reverse — What if we did the opposite? |

| Skill | Description |
|-------|-------------|
| `brainstorm` | Quick divergent ideation across all dimensions |
| `workshop` | Step through each SCAMPER dimension interactively |

**Example:**

```
You: /scamper workshop my checkout flow

Claude: Let's SCAMPER your checkout flow. Starting with Substitute...

**S - Substitute**
- What if we substituted the multi-page form with a single-page experience?
- What if we replaced email confirmation with SMS?
- What if we substituted manual address entry with address autocomplete?

Ready to explore Combine? (yes/skip)
```

**Use case:** Improving an existing feature? Run a SCAMPER workshop on your current implementation to systematically explore every angle for improvement.

---

### question-storm

**Reframe problems through rapid question generation.**

Implements the Question Storming framework—a brainstorming technique focused on generating questions rather than answers. Uncover blind spots, challenge assumptions, and find new angles.

| Skill | Description |
|-------|-------------|
| `brainstorm` | Rapid-fire question generation (divergent) |
| `workshop` | Interactive session exploring questions deeply |

**Example:**

```
You: Help me question-storm our API rate limiting approach

Claude: Here are 15 questions to reframe your thinking:

1. What happens when legitimate users hit the limit?
2. Are all endpoints equally valuable to protect?
3. What if rate limits encouraged bad patterns (batching vs real-time)?
4. How do competitors handle this?
5. What's the cost of NOT rate limiting vs over-limiting?
...
```

**Use case:** Stuck on a technical decision? Run a question storm to surface what you haven't considered: "What would break if we chose X?" "Who else is affected?" "What are we assuming?"

---

## Installation

### Add the Marketplace

```bash
claude plugin marketplace add https://github.com/sofrono44/sofrono-plugins
```

### Install Individual Plugins

```bash
claude plugin install finra-review-skill@sofrono-plugins
claude plugin install spec-to-ralph@sofrono-plugins
claude plugin install question-storm@sofrono-plugins
claude plugin install scamper@sofrono-plugins
```

### Verify Installation

```bash
claude plugin list
```

---

## Roadmap

- [ ] More ideation frameworks (Six Thinking Hats, First Principles)
- [ ] Template library for common Spec Kit patterns
- [ ] Export workshop sessions to markdown
- [ ] Team sharing for brainstorm outputs

Have an idea? [Open an issue](https://github.com/sofrono44/sofrono-plugins/issues)!

---

## Contributing

Contributions welcome! Whether it's:

- Bug reports
- Feature suggestions
- Documentation improvements
- New plugin ideas

---

## License

MIT © [sofrono44](https://github.com/sofrono44)

---

<div align="center">
  <sub>Built for the Claude Code community</sub>
</div>
