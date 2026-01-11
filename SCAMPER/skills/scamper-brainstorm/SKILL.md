---
name: scamper-brainstorm
description: Generate rapid divergent ideas using the SCAMPER framework. Use when users want to brainstorm, ideate, innovate, or explore variations on a concept, product, business model, feature, pitch, or strategy. Triggers include phrases like "brainstorm ideas for", "how could I improve", "variations on", "innovate on", "riff on", "SCAMPER", or requests to explore alternatives to an existing concept.
---

# SCAMPER Brainstorm

Generate comprehensive idea variations across all seven SCAMPER dimensions in a single output.

## SCAMPER Framework

| Letter | Dimension | Core Question |
|--------|-----------|---------------|
| S | Substitute | What components, materials, people, or processes could be replaced? |
| C | Combine | What could be merged, integrated, or bundled together? |
| A | Adapt | What else is like this? What could be borrowed from other domains? |
| M | Modify | What could be magnified, minimized, or altered in form? |
| P | Put to other uses | What else could this be used for? Who else could use it? |
| E | Eliminate | What could be removed, simplified, or stripped away? |
| R | Reverse/Rearrange | What if the order, direction, or roles were flipped? |

## Execution

### 1. Identify the focal concept
Extract the core idea, product, or strategy to workshop. Restate it in one sentence to confirm understanding.

### 2. Detect domain context
Infer the relevant industry or domain (fintech, B2B SaaS, consumer, regulated industries, etc.) to calibrate suggestions appropriately.

### 3. Generate ideas for each dimension
For each SCAMPER letter, produce 3-5 concrete, actionable suggestions. Prioritize:
- Specificity over vagueness
- Surprising combinations over obvious ones
- Feasibility within the detected domain constraints

### 4. Synthesize
End with a "Most Promising Mutations" section highlighting 2-4 ideas that:
- Combine multiple SCAMPER dimensions
- Address an unmet need or competitive gap
- Are non-obvious but achievable

## Output Format

```markdown
# SCAMPER Brainstorm: [Concept Name]

**Focal concept:** [One-sentence restatement]
**Domain context:** [Detected industry/constraints]

---

## S — Substitute
- [Idea 1]
- [Idea 2]
- [Idea 3]

## C — Combine
- [Idea 1]
- [Idea 2]
- [Idea 3]

## A — Adapt
- [Idea 1]
- [Idea 2]
- [Idea 3]

## M — Modify
- [Idea 1]
- [Idea 2]
- [Idea 3]

## P — Put to Other Uses
- [Idea 1]
- [Idea 2]
- [Idea 3]

## E — Eliminate
- [Idea 1]
- [Idea 2]
- [Idea 3]

## R — Reverse/Rearrange
- [Idea 1]
- [Idea 2]
- [Idea 3]

---

## Most Promising Mutations

1. **[Name]**: [Brief description of why this is high-potential]
2. **[Name]**: [Brief description]
3. **[Name]**: [Brief description]
```

## Domain Calibration Examples

**Fintech/Capital Markets**: Consider regulatory constraints, API integration patterns, compliance workflows, custody and settlement implications.

**B2B Infrastructure**: Consider integration complexity, enterprise sales cycles, platform dynamics, developer experience.

**Consumer Products**: Consider distribution channels, virality mechanics, retention loops, monetization models.

## Tips

- If the concept is vague, ask one clarifying question before generating.
- Bold the most provocative idea in each section.
- Cross-reference ideas across dimensions when natural (e.g., "This connects to the 'Combine' idea above").
