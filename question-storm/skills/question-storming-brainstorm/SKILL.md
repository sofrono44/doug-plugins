---
name: question-storming-brainstorm
description: Generate a rapid burst of questions to reframe a problem or challenge. Use when users want to explore a problem space, uncover assumptions, find new angles, or "question storm" an idea. Triggers include phrases like "what questions should I ask", "help me think about this differently", "what am I missing", "reframe this problem", "question storm", or requests to challenge assumptions about a concept.
---

# Question Storming Brainstorm

Generate a comprehensive set of questions across multiple question types to open up a problem space and surface hidden assumptions.

## Question Storming Framework

| Type | Purpose | Example Starter |
|------|---------|-----------------|
| Why | Uncover root causes and assumptions | "Why do we assume...?" |
| What if | Explore counterfactuals and possibilities | "What if the opposite were true?" |
| How might we | Reframe constraints as opportunities | "How might we turn this weakness into...?" |
| What's stopping | Surface blockers and hidden constraints | "What's stopping us from...?" |
| Who else | Find analogies and adjacent solutions | "Who else has solved a similar problem?" |
| What would have to be true | Test hypotheses and validate assumptions | "What would have to be true for this to work?" |

## Execution

### 1. Identify the focal challenge
Extract the core problem, decision, or situation to question. Restate it in one sentence to confirm understanding.

### 2. Detect domain context
Infer the relevant industry or domain to calibrate question framing appropriately.

### 3. Generate questions for each type
For each question type, produce 3-5 questions. Prioritize:
- Questions that challenge unstated assumptions
- Questions that reframe the problem entirely
- Questions that surface hidden stakeholders or constraints
- Surprising angles over obvious ones

### 4. Synthesize
End with a "Most Generative Questions" section highlighting 3-5 questions that:
- Reframe the problem in a useful new way
- Challenge a core assumption
- Open up non-obvious solution paths

## Output Format

```markdown
# Question Storm: [Challenge Name]

**Focal challenge:** [One-sentence restatement]
**Domain context:** [Detected industry/constraints]

---

## Why Questions
- [Question 1]
- [Question 2]
- [Question 3]

## What If Questions
- [Question 1]
- [Question 2]
- [Question 3]

## How Might We Questions
- [Question 1]
- [Question 2]
- [Question 3]

## What's Stopping Questions
- [Question 1]
- [Question 2]
- [Question 3]

## Who Else Questions
- [Question 1]
- [Question 2]
- [Question 3]

## What Would Have to Be True Questions
- [Question 1]
- [Question 2]
- [Question 3]

---

## Most Generative Questions

1. **[Question]**: [Why this question is powerful—what assumption it challenges or path it opens]
2. **[Question]**: [Why this question is powerful]
3. **[Question]**: [Why this question is powerful]
```

## Domain Calibration Examples

**Fintech/Capital Markets**: Question regulatory assumptions, distribution channel constraints, trust/custody dynamics, integration dependencies, competitive moats.

**B2B Infrastructure**: Question buyer personas, build-vs-buy decisions, platform lock-in, adoption friction, pricing model assumptions.

**Fundraising/Strategy**: Question narrative framing, market timing assumptions, competitive positioning, team composition requirements.

**Product Development**: Question user needs assumptions, prioritization logic, technical feasibility, go-to-market sequencing.

## Tips

- If the challenge is vague, ask one clarifying question before generating.
- **Bold** the most assumption-challenging question in each section.
- Look for questions that make the user uncomfortable—those often surface real constraints.
- Cross-reference questions when natural (e.g., "This 'Who else' question connects to the 'What if' above").
