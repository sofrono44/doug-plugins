---
name: scamper-workshop
description: Facilitate an interactive SCAMPER ideation session, exploring one dimension at a time conversationally. Use when users want to "workshop an idea", "think through" a concept together, have a "brainstorming session", do "deep ideation", or explicitly request interview-style or conversational exploration of variations. Also triggers on "let's SCAMPER this" or "walk me through SCAMPER".
---

# SCAMPER Workshop (Interview Mode)

Guide users through an interactive SCAMPER session, one dimension at a time, building on their reactions.

## SCAMPER Framework

| Letter | Dimension | Core Question |
|--------|-----------|---------------|
| S | Substitute | What could be replaced? |
| C | Combine | What could be merged? |
| A | Adapt | What could be borrowed from elsewhere? |
| M | Modify | What could be scaled up, down, or changed? |
| P | Put to other uses | Who else could use this? What else could it do? |
| E | Eliminate | What could be removed? |
| R | Reverse/Rearrange | What if we flipped it? |

## Session Flow

### 1. Open
Confirm the concept to workshop. Restate it and ask if the framing is right.

Example: "So we're workshopping Switchfin as MCP middleware for capital markets. Before we dive in—is there a specific angle you want to stress-test, or should we explore broadly?"

### 2. Work through each dimension
Present 2-3 ideas for the current dimension. Wait for reaction. Based on response:
- If excited → drill deeper on that thread before moving on
- If lukewarm → note it and advance to next dimension
- If they have their own riff → explore it together

Transition phrase: "Ready to move to [Next Letter] — [Dimension]? Or want to keep pulling on this thread?"

### 3. Track momentum
Maintain a mental (or explicit) shortlist of ideas that sparked interest. Reference them when relevant in later dimensions.

Example: "This connects back to the 'Combine with compliance' idea you liked earlier..."

### 4. Synthesize at the end
Offer to compile a summary document of:
- All explored ideas by dimension
- Starred/highlighted ideas based on user reactions
- Suggested next steps or validation questions

## Pacing Guidelines

- Spend 1-3 exchanges per dimension depending on energy
- Don't force all seven if the user finds gold early—offer to go deep instead
- If user seems fatigued, offer to pause and resume later or switch to brainstorm mode for remaining dimensions

## Conversation Patterns

**Opening a dimension:**
> "Let's try **[Letter] — [Dimension]**. The core question here is: [question]. A few ideas to react to..."

**Reading interest:**
> "You seemed most interested in [X]. Want to explore variations on that before we move on?"

**Bridging dimensions:**
> "That 'Eliminate' idea—stripping out the middleware layer—actually sets up an interesting 'Reverse' question: what if the broker-dealers built the integration themselves and you licensed the spec?"

**Offering synthesis:**
> "We've hit all seven. Want me to compile the highlights into a doc? I can include the threads you were most drawn to and some validation questions."

## Domain Awareness

Adapt suggestions to user's context:
- **Fintech**: regulatory constraints, clearing/settlement, API integrations
- **B2B infra**: enterprise sales, platform dynamics, developer adoption
- **Fundraising**: narrative framing, investor psychology, market timing

## Output Option

At session end, offer to generate a markdown summary:

```markdown
# SCAMPER Workshop Summary: [Concept]

**Date:** [Date]
**Focus:** [Any specific angle]

## Explored Ideas

### S — Substitute
- [Idea] ⭐ (user highlighted)
- [Idea]

### C — Combine
- [Idea]
- [Idea] ⭐

[...continue for each dimension worked...]

## Top Threads
1. [Idea name]: [Why it resonated]
2. [Idea name]: [Why it resonated]

## Suggested Next Steps
- [ ] Validate [idea] with [specific action]
- [ ] Prototype [idea]
- [ ] Test [idea] in pitch to [audience]
```
