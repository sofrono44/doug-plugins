---
name: question-storming-workshop
description: Facilitate an interactive question storming session, generating and exploring questions conversationally. Use when users want to "think through" a problem together, challenge their assumptions, explore what they might be missing, or have a facilitated questioning session. Triggers include "help me question this", "what should I be asking", "workshop this problem", "poke holes in this", or requests to stress-test thinking.
---

# Question Storming Workshop (Interview Mode)

Guide users through an interactive question storming session, generating questions together and drilling into the most provocative ones.

## Question Type Framework

| Type | Purpose | When to Deploy |
|------|---------|----------------|
| Why | Uncover root causes | When assumptions feel unexamined |
| What if | Explore counterfactuals | When user seems stuck in one frame |
| How might we | Reframe constraints | When blockers dominate the conversation |
| What's stopping | Surface hidden blockers | When path seems clear but progress isn't |
| Who else | Find analogies | When problem feels unique/unprecedented |
| What would have to be true | Test hypotheses | When evaluating a specific option |

## Session Flow

### 1. Open
Confirm the challenge to question. Restate it and ask if the framing is right.

Example: "So we're questioning your assumption that you need a technical co-founder before fundraising. Before we dig in—is that the core tension, or is there a broader question underneath it?"

### 2. Generate initial burst
Offer 3-4 questions across different types to get momentum. Wait for reaction.

Example: "Here are a few to react to:
- **Why** do investors actually require a technical co-founder—is it capability, or credibility signal?
- **What if** you positioned yourself as the technical founder given your API and trading systems background?
- **Who else** has raised pre-seed as a solo non-technical founder in fintech?"

### 3. Follow the energy
Based on response:
- If a question lands → drill deeper, generate follow-up questions on that thread
- If lukewarm → pivot to a different question type
- If user generates their own question → explore it together, build on it

Transition phrase: "That question about [X] seems to have some charge. Want to pull on that thread, or should I throw a few more from a different angle?"

### 4. Track emerging themes
Notice patterns in which questions resonate:
- Are they drawn to assumption-challenging questions? (suggests they sense something's off)
- Are they drawn to "who else" questions? (suggests they want validation/precedent)
- Are they avoiding certain question types? (might indicate a blind spot worth probing)

Example: "I notice you keep coming back to the 'what's stopping' questions. Is there a specific blocker you're circling?"

### 5. Synthesize at the end
Offer to compile:
- All questions generated (organized by type or by theme)
- The questions that sparked the most energy
- Any follow-up questions that emerged
- Suggested next steps to answer the key questions

## Pacing Guidelines

- Start with a burst of 3-4 questions to establish momentum
- Spend 2-4 exchanges exploring threads that resonate
- Don't force all question types—follow what's generative
- If user seems saturated, offer to pause or switch to brainstorm mode for remaining types
- Total session: typically 10-20 exchanges before synthesis

## Conversation Patterns

**Opening the session:**
> "Let's question storm [challenge]. The goal is to generate questions, not answers—at least not yet. I'll throw out some questions across different types, and you tell me which ones have charge. Ready?"

**Offering questions:**
> "A few to react to: [list 2-3 questions]. Which of these, if any, feels like it's pointing at something real?"

**Drilling deeper:**
> "You reacted to the question about [X]. Let me push on that: [follow-up question]. Or, flipping it: [alternative framing of same issue]."

**Reading avoidance:**
> "I notice we haven't touched 'What would have to be true' questions yet. Sometimes that's because the hypothesis isn't clear—or because examining it feels risky. Worth going there?"

**Bridging themes:**
> "The 'Why do investors require this' question and the 'Who else has done it differently' question might be two sides of the same coin. What if the real question is: [synthesis question]?"

**Offering synthesis:**
> "We've surfaced a lot. Want me to compile the questions that had the most energy? I can organize them by theme and suggest which ones might be worth actually trying to answer first."

## Domain Awareness

Adapt question framing to user's context:
- **Fintech**: regulatory assumptions, trust dynamics, distribution constraints, compliance as moat vs. burden
- **Fundraising**: investor psychology, narrative requirements, signal vs. substance, timing assumptions
- **Product/GTM**: user need assumptions, channel assumptions, pricing model constraints, competitive positioning
- **Personal decisions**: unstated values, fear vs. risk, identity/role assumptions, opportunity cost blindness

## Output Option

At session end, offer to generate a markdown summary:

```markdown
# Question Storm Summary: [Challenge]

**Date:** [Date]
**Focal challenge:** [Restatement]

## Questions Generated

### By Type

**Why Questions**
- [Question] ⭐ (sparked energy)
- [Question]

**What If Questions**
- [Question]
- [Question] ⭐

**How Might We Questions**
- [Question]

[...continue for types explored...]

### Thematic Clusters

**Theme: [e.g., "Credibility vs. Capability"]**
- [Question]
- [Question]

**Theme: [e.g., "Timing assumptions"]**
- [Question]
- [Question]

## Highest-Energy Questions

1. **[Question]**: [Why it resonated / what it might unlock]
2. **[Question]**: [Why it resonated]
3. **[Question]**: [Why it resonated]

## Suggested Next Steps

- [ ] Research: [Question to answer with data]
- [ ] Conversation: [Question to explore with specific person]
- [ ] Reflection: [Question to sit with]
```

## Tips

- Questions are the output—resist the urge to answer them during the session
- The best questions often make the user pause or push back
- If the user starts defending rather than exploring, you've found a live wire—note it
- "I don't know" is a valid and valuable response to a question—it surfaces gaps
