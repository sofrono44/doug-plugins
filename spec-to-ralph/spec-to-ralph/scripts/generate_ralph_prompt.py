#!/usr/bin/env python3
"""
generate_ralph_prompt.py - Generate Ralph PROMPT.md from Spec Kit project

Supports both flat and feature-based Spec Kit structures.

Usage:
    python generate_ralph_prompt.py [project_path] [options]

Options:
    --feature FEATURES    Feature selection: 'all', single ID, or comma-separated list
    --max-iterations N    Override auto-calculated iterations
    --json                Output results as JSON
"""

import argparse
import os
import re
import sys
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, List, Tuple, Dict


@dataclass
class Feature:
    """Single feature from Spec Kit"""
    id: str                          # e.g., "001-user-auth"
    number: str                       # e.g., "001"
    name: str                         # e.g., "user-auth"
    path: Path                        # Full path to feature directory
    spec: Optional[str] = None
    plan: Optional[str] = None
    tasks: Optional[str] = None
    task_count: int = 0
    incomplete_tasks: int = 0
    issues: List[str] = field(default_factory=list)


@dataclass
class SpecKitProject:
    """Parsed Spec Kit project structure"""
    root: Path
    structure: str = "unknown"        # "flat" or "features"
    constitution: Optional[str] = None
    
    # For flat structure
    spec: Optional[str] = None
    plan: Optional[str] = None
    tasks: Optional[str] = None
    
    # For feature structure
    features: List[Feature] = field(default_factory=list)
    selected_features: List[Feature] = field(default_factory=list)
    
    # Computed
    total_tasks: int = 0
    total_incomplete: int = 0
    backpressure_commands: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    tech_stack: str = "unknown"
    issues: List[str] = field(default_factory=list)


def read_file_safe(path: Optional[Path]) -> Optional[str]:
    """Safely read file contents"""
    if path is None or not path.exists():
        return None
    try:
        return path.read_text(encoding='utf-8')
    except Exception:
        return None


def parse_feature_id(dirname: str) -> Tuple[str, str]:
    """Parse feature directory name into number and name"""
    match = re.match(r'^(\d+)-(.+)$', dirname)
    if match:
        return match.group(1), match.group(2)
    # No number prefix
    return "", dirname


def discover_features(specify_dir: Path) -> List[Feature]:
    """Discover all features in .specify/features/"""
    features_dir = specify_dir / "features"
    if not features_dir.exists():
        return []
    
    features = []
    for item in sorted(features_dir.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            number, name = parse_feature_id(item.name)
            feature = Feature(
                id=item.name,
                number=number,
                name=name,
                path=item,
                spec=read_file_safe(item / "spec.md"),
                plan=read_file_safe(item / "plan.md"),
                tasks=read_file_safe(item / "tasks.md")
            )
            
            # Analyze tasks
            if feature.tasks:
                feature.task_count, feature.incomplete_tasks, issues = analyze_tasks(feature.tasks)
                feature.issues.extend(issues)
            
            # Check for missing files
            if not feature.tasks:
                feature.issues.append("Missing tasks.md (required)")
            if not feature.spec:
                feature.issues.append("Missing spec.md (recommended)")
            if not feature.plan:
                feature.issues.append("Missing plan.md (recommended)")
            
            features.append(feature)
    
    return features


def match_feature(features: List[Feature], selector: str) -> Optional[Feature]:
    """Match a feature by number, name, or full id"""
    selector = selector.strip().lower()
    
    for f in features:
        if f.id.lower() == selector:
            return f
        if f.number == selector:
            return f
        if f.name.lower() == selector:
            return f
        # Partial match on name
        if selector in f.name.lower():
            return f
    
    return None


def resolve_feature_selection(features: List[Feature], selection: Optional[str]) -> Tuple[List[Feature], List[str]]:
    """Resolve feature selection string to list of features"""
    errors = []
    
    if not features:
        return [], ["No features found in .specify/features/"]
    
    if selection is None or selection == "":
        # Auto-select: if one feature, use it; otherwise require explicit selection
        if len(features) == 1:
            return features, []
        else:
            return [], [f"Multiple features found. Please specify --feature: {', '.join(f.id for f in features)}"]
    
    if selection.lower() == "all":
        return features, []
    
    # Parse comma-separated list
    selected = []
    for selector in selection.split(','):
        selector = selector.strip()
        if not selector:
            continue
        
        matched = match_feature(features, selector)
        if matched:
            if matched not in selected:
                selected.append(matched)
        else:
            errors.append(f"Feature not found: '{selector}'")
    
    return selected, errors


def analyze_tasks(tasks_content: str) -> Tuple[int, int, List[str]]:
    """Analyze tasks for count and potential issues"""
    if not tasks_content:
        return 0, 0, ["No tasks content"]
    
    issues = []
    
    # Count checkboxes
    incomplete = len(re.findall(r'- \[ \]', tasks_content))
    complete = len(re.findall(r'- \[x\]', tasks_content, re.I))
    total = incomplete + complete
    
    # If no checkboxes, count numbered items
    if total == 0:
        numbered = re.findall(r'^\d+\.\s+(.+)$', tasks_content, re.MULTILINE)
        total = len(numbered)
        incomplete = total
    
    # Check for large tasks
    task_lines = re.findall(r'- \[ \]\s*(.+)', tasks_content)
    for task in task_lines:
        and_count = task.lower().count(' and ')
        if and_count >= 2:
            issues.append(f"Large task (multiple 'and'): {task[:60]}...")
    
    return total, incomplete, issues


def extract_constraints(constitution: str) -> List[str]:
    """Extract non-negotiable constraints from constitution"""
    if not constitution:
        return []
    
    constraints = []
    lines = constitution.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Extract bullet points and numbered items
        match = re.match(r'^[-*]\s+(.+)$', line) or re.match(r'^\d+\.\s+(.+)$', line)
        if match:
            content = match.group(1).strip().rstrip('.')
            if content and len(content) > 10:
                constraints.append(content)
    
    # Deduplicate
    seen = set()
    unique = []
    for c in constraints:
        key = c.lower()[:50]
        if key not in seen:
            seen.add(key)
            unique.append(c)
    
    return unique[:15]


def detect_tech_stack(plan: str, constitution: str) -> Tuple[str, List[str]]:
    """Detect tech stack and appropriate backpressure commands"""
    combined = ((plan or "") + (constitution or "")).lower()
    
    commands = []
    stack = "unknown"
    
    # Check for explicit commands first
    explicit_test = re.search(r'test\s*(?:command|cmd)?[:\s]+[`"]?([^`"\n]+)[`"]?', combined)
    explicit_lint = re.search(r'lint\s*(?:command|cmd)?[:\s]+[`"]?([^`"\n]+)[`"]?', combined)
    
    if explicit_test:
        commands.append(explicit_test.group(1).strip())
    if explicit_lint:
        commands.append(explicit_lint.group(1).strip())
    
    # Stack detection with defaults
    if any(x in combined for x in ['typescript', 'node', 'npm', 'react', 'next.js', 'javascript']):
        stack = "node"
        if not explicit_test:
            commands.append("npm test")
        if not explicit_lint:
            commands.append("npm run lint")
        if 'typescript' in combined:
            commands.append("npm run build")
    
    elif any(x in combined for x in ['python', 'django', 'flask', 'fastapi', 'pytest']):
        stack = "python"
        if not explicit_test:
            commands.append("pytest")
        if not explicit_lint:
            commands.append("ruff check .")
    
    elif any(x in combined for x in ['rust', 'cargo']):
        stack = "rust"
        if not explicit_test:
            commands.append("cargo test")
        commands.append("cargo clippy")
        commands.append("cargo build")
    
    elif any(x in combined for x in ['golang', 'go mod', 'go test', ' go ']):
        stack = "go"
        if not explicit_test:
            commands.append("go test ./...")
        commands.append("go vet ./...")
    
    # Fallback
    if not commands:
        commands = ["# TODO: Add test command", "# TODO: Add lint command"]
    
    return stack, list(dict.fromkeys(commands))


def calculate_iterations(incomplete_tasks: int, num_features: int = 1, buffer: float = 0.2) -> int:
    """Calculate recommended max iterations"""
    base = incomplete_tasks * 4
    # Add extra iterations for feature transitions
    if num_features > 1:
        base += (num_features - 1) * 5
    with_buffer = int(base * (1 + buffer))
    return min(max(with_buffer, 10), 100)  # Min 10, max 100


def generate_prompt_flat(project: SpecKitProject) -> str:
    """Generate prompt for flat structure"""
    project_name = project.root.name or "Project"
    
    constraints_text = "\n".join(f"- {c}" for c in project.constraints[:10]) if project.constraints else "- Follow all guidelines in constitution.md"
    backpressure_text = "\n".join(f"   {cmd}" for cmd in project.backpressure_commands)
    
    return f'''# Ralph Loop: {project_name}

## Context

Before starting, read these files to understand the project:
- `@.specify/constitution.md` - Non-negotiable rules you MUST follow
- `@.specify/spec.md` - What we're building and acceptance criteria
- `@.specify/plan.md` - Technical approach and architecture

## Your Mission

Complete all tasks in `.specify/tasks.md` systematically until done.

## Process (Every Iteration)

1. **Read Tasks**: Check `@.specify/tasks.md` for the next `- [ ]` unchecked task

2. **Search First**: Before implementing, search the codebase
   - Use grep/find to locate related code
   - Check if similar functionality already exists

3. **Implement**: Make the minimal changes needed for this ONE task

4. **Verify**: Run ALL feedback loops - every one must pass:
```bash
{backpressure_text}
```

5. **Mark Complete**: Change `- [ ]` to `- [x]` for this task in tasks.md

6. **Commit**: `git add -A && git commit -m "feat: [task description]"`

7. **Continue**: Return to step 1 for the next unchecked task

## Constraints (Non-Negotiable)

{constraints_text}

## Completion Signals

All tasks done + tests pass:
<promise>ALL_TASKS_COMPLETE</promise>

Unable to progress after 10 iterations:
<promise>BLOCKED</promise>

## If Stuck

After 5 attempts on one task:
1. Add `BLOCKED:` prefix to the task
2. Document what you tried
3. Move to the next task
'''


def generate_prompt_single_feature(project: SpecKitProject, feature: Feature) -> str:
    """Generate prompt for single feature"""
    project_name = project.root.name or "Project"
    
    constraints_text = "\n".join(f"- {c}" for c in project.constraints[:10]) if project.constraints else "- Follow all guidelines in constitution.md"
    backpressure_text = "\n".join(f"   {cmd}" for cmd in project.backpressure_commands)
    
    return f'''# Ralph Loop: {project_name} - Feature {feature.id}

## Context

Before starting, read these files:
- `@.specify/constitution.md` - Global rules (apply to all features)
- `@.specify/features/{feature.id}/spec.md` - This feature's specification
- `@.specify/features/{feature.id}/plan.md` - This feature's technical plan

## Your Mission

Complete all tasks in `.specify/features/{feature.id}/tasks.md`

Current status: {feature.incomplete_tasks} tasks remaining

## Process (Every Iteration)

1. **Read Tasks**: Check `@.specify/features/{feature.id}/tasks.md` for the next `- [ ]` unchecked task

2. **Search First**: Before implementing, search the codebase
   - Use grep/find to locate related code
   - Check if similar functionality already exists

3. **Implement**: Make the minimal changes needed for this ONE task

4. **Verify**: Run ALL feedback loops - every one must pass:
```bash
{backpressure_text}
```

5. **Mark Complete**: Change `- [ ]` to `- [x]` for this task

6. **Commit**: `git add -A && git commit -m "feat({feature.name}): [task description]"`

7. **Continue**: Return to step 1 for the next unchecked task

## Constraints (Non-Negotiable)

{constraints_text}

## Completion Signals

All tasks in this feature done + tests pass:
<promise>ALL_TASKS_COMPLETE</promise>

Unable to progress after 10 iterations:
<promise>BLOCKED</promise>

## If Stuck

After 5 attempts on one task:
1. Add `BLOCKED:` prefix to the task
2. Document what you tried
3. Move to the next task
'''


def generate_prompt_multi_feature(project: SpecKitProject) -> str:
    """Generate prompt for multiple features"""
    project_name = project.root.name or "Project"
    features = project.selected_features
    
    constraints_text = "\n".join(f"- {c}" for c in project.constraints[:10]) if project.constraints else "- Follow all guidelines in constitution.md"
    backpressure_text = "\n".join(f"   {cmd}" for cmd in project.backpressure_commands)
    
    # Build feature list
    feature_list = []
    for i, f in enumerate(features, 1):
        feature_list.append(f"{i}. `{f.id}` ({f.incomplete_tasks} tasks)")
    feature_list_text = "\n".join(feature_list)
    
    # Build context list
    context_list = ["- `@.specify/constitution.md` - Global rules (apply to all features)"]
    for f in features:
        context_list.append(f"- `@.specify/features/{f.id}/` - spec.md, plan.md, tasks.md")
    context_text = "\n".join(context_list)
    
    return f'''# Ralph Loop: {project_name} - Multiple Features

## Features to Complete (in order)

{feature_list_text}

Total: {project.total_incomplete} tasks across {len(features)} features

## Context

{context_text}

## Your Mission

Complete all features in the order listed above. For each feature:
1. Read its spec.md and plan.md
2. Complete ALL tasks in its tasks.md
3. Only move to the next feature when current is 100% complete

## Process (Every Iteration)

1. **Identify Current Feature**: Find the first feature with incomplete tasks

2. **Read Tasks**: Check that feature's tasks.md for the next `- [ ]` task

3. **Search First**: Before implementing, search the codebase

4. **Implement**: Make the minimal changes needed for this ONE task

5. **Verify**: Run ALL feedback loops - every one must pass:
```bash
{backpressure_text}
```

6. **Mark Complete**: Change `- [ ]` to `- [x]` for this task

7. **Commit**: `git add -A && git commit -m "feat([feature-name]): [task description]"`

8. **Continue**: 
   - If more tasks in current feature → next task
   - If feature complete → move to next feature
   - If all features complete → output completion signal

## Constraints (Non-Negotiable)

{constraints_text}

## Completion Signals

All features complete + tests pass:
<promise>ALL_TASKS_COMPLETE</promise>

Single feature complete (for progress tracking):
<promise>FEATURE_COMPLETE: [feature-id]</promise>

Unable to progress after 10 iterations:
<promise>BLOCKED</promise>

## If Stuck

After 5 attempts on one task:
1. Add `BLOCKED:` prefix to the task
2. Document what you tried
3. Move to the next task (same or next feature)
'''


def generate_config(project: SpecKitProject, max_iterations: int) -> str:
    """Generate ralph-config.md"""
    
    if project.structure == "features" and project.selected_features:
        feature_info = "\n".join(
            f"  - {f.id}: {f.incomplete_tasks} tasks"
            for f in project.selected_features
        )
        scope_info = f"Features included:\n{feature_info}"
    else:
        scope_info = f"Scope: All tasks in .specify/tasks.md"
    
    return f'''# Ralph Configuration: {project.root.name}

## Quick Start

```bash
/ralph-loop "Follow PROMPT.md to complete all tasks" \\
  --max-iterations {max_iterations} \\
  --completion-promise "ALL_TASKS_COMPLETE"
```

## Configuration

| Setting | Value |
|---------|-------|
| Max Iterations | {max_iterations} |
| Tech Stack | {project.tech_stack} |
| Total Tasks | {project.total_incomplete} incomplete / {project.total_tasks} total |

{scope_info}

## Backpressure Commands

```bash
{chr(10).join(project.backpressure_commands)}
```

## Pre-Flight Checklist

- [ ] Review tasks - well-defined?
- [ ] Run backpressure commands manually - working?
- [ ] Git clean? `git add -A && git commit -m "pre-ralph checkpoint"`

## Recovery

```bash
/cancel-ralph              # Stop the loop
git diff                   # See changes
git reset --hard HEAD~1    # Revert last commit
```
'''


def analyze_project(project_path: Path, feature_selection: Optional[str] = None) -> SpecKitProject:
    """Full project analysis"""
    project = SpecKitProject(root=project_path)
    specify_dir = project_path / ".specify"
    
    if not specify_dir.exists():
        project.issues.append(".specify/ directory not found")
        return project
    
    # Load constitution (always at root)
    project.constitution = read_file_safe(specify_dir / "constitution.md")
    if not project.constitution:
        project.issues.append("Missing constitution.md (recommended)")
    
    # Detect structure
    features_dir = specify_dir / "features"
    flat_tasks = specify_dir / "tasks.md"
    
    if features_dir.exists() and any(features_dir.iterdir()):
        project.structure = "features"
        project.features = discover_features(specify_dir)
        
        # Resolve feature selection
        selected, errors = resolve_feature_selection(project.features, feature_selection)
        project.selected_features = selected
        project.issues.extend(errors)
        
        # Aggregate stats from selected features
        for f in selected:
            project.total_tasks += f.task_count
            project.total_incomplete += f.incomplete_tasks
            project.issues.extend([f"[{f.id}] {issue}" for issue in f.issues])
        
        # Get plan content for tech detection (from first feature with plan)
        plan_content = ""
        for f in selected:
            if f.plan:
                plan_content = f.plan
                break
        
        project.tech_stack, project.backpressure_commands = detect_tech_stack(
            plan_content, project.constitution or ""
        )
    
    elif flat_tasks.exists():
        project.structure = "flat"
        project.spec = read_file_safe(specify_dir / "spec.md")
        project.plan = read_file_safe(specify_dir / "plan.md")
        project.tasks = read_file_safe(flat_tasks)
        
        if project.tasks:
            project.total_tasks, project.total_incomplete, issues = analyze_tasks(project.tasks)
            project.issues.extend(issues)
        else:
            project.issues.append("tasks.md is empty")
        
        project.tech_stack, project.backpressure_commands = detect_tech_stack(
            project.plan or "", project.constitution or ""
        )
    
    else:
        project.issues.append("No tasks.md or features/ found in .specify/")
    
    # Extract constraints
    if project.constitution:
        project.constraints = extract_constraints(project.constitution)
    
    return project


def main():
    parser = argparse.ArgumentParser(
        description="Generate Ralph prompts from Spec Kit projects"
    )
    parser.add_argument("project_path", type=Path, nargs="?", default=Path("."),
                        help="Path to project root (default: current directory)")
    parser.add_argument("--feature", type=str, default=None,
                        help="Feature selection: 'all', single ID, or comma-separated list")
    parser.add_argument("--max-iterations", type=int, default=None,
                        help="Override max iterations")
    parser.add_argument("--json", action="store_true",
                        help="Output as JSON")
    
    args = parser.parse_args()
    project_path = args.project_path.resolve()
    
    if not project_path.exists():
        print(f"Error: Path does not exist: {project_path}", file=sys.stderr)
        sys.exit(1)
    
    # Analyze
    project = analyze_project(project_path, args.feature)
    
    # Check for fatal errors
    if project.total_incomplete == 0 and not project.tasks:
        print("Error: No tasks found", file=sys.stderr)
        for issue in project.issues:
            print(f"  - {issue}", file=sys.stderr)
        sys.exit(1)
    
    # Calculate iterations
    num_features = len(project.selected_features) if project.structure == "features" else 1
    max_iter = args.max_iterations or calculate_iterations(project.total_incomplete, num_features)
    
    # Generate prompt based on structure
    if project.structure == "flat":
        prompt_content = generate_prompt_flat(project)
    elif len(project.selected_features) == 1:
        prompt_content = generate_prompt_single_feature(project, project.selected_features[0])
    else:
        prompt_content = generate_prompt_multi_feature(project)
    
    config_content = generate_config(project, max_iter)
    
    # Write files
    prompt_path = project_path / "PROMPT.md"
    config_path = project_path / "ralph-config.md"
    
    prompt_path.write_text(prompt_content, encoding='utf-8')
    config_path.write_text(config_content, encoding='utf-8')
    
    if args.json:
        result = {
            "success": True,
            "structure": project.structure,
            "files": {
                "prompt": str(prompt_path),
                "config": str(config_path)
            },
            "features": [
                {"id": f.id, "tasks": f.task_count, "incomplete": f.incomplete_tasks}
                for f in project.selected_features
            ] if project.structure == "features" else None,
            "analysis": {
                "tech_stack": project.tech_stack,
                "total_tasks": project.total_tasks,
                "incomplete_tasks": project.total_incomplete,
                "max_iterations": max_iter,
                "backpressure_commands": project.backpressure_commands
            },
            "issues": project.issues,
            "command": f'/ralph-loop "Follow PROMPT.md" --max-iterations {max_iter} --completion-promise "ALL_TASKS_COMPLETE"'
        }
        print(json.dumps(result, indent=2))
    else:
        print(f"✅ Generated: {prompt_path}")
        print(f"✅ Generated: {config_path}")
        print()
        print(f"📁 Structure: {project.structure}")
        
        if project.structure == "features" and project.selected_features:
            print(f"📋 Features selected:")
            for f in project.selected_features:
                print(f"   - {f.id}: {f.incomplete_tasks}/{f.task_count} tasks")
        
        print(f"\n📊 Summary:")
        print(f"   Tech Stack: {project.tech_stack}")
        print(f"   Tasks: {project.total_incomplete} incomplete / {project.total_tasks} total")
        print(f"   Max Iterations: {max_iter}")
        
        if project.issues:
            print(f"\n⚠️  Issues:")
            for issue in project.issues[:5]:
                print(f"   - {issue}")
            if len(project.issues) > 5:
                print(f"   ... and {len(project.issues) - 5} more")
        
        print(f"\n🚀 Run:")
        print(f'   /ralph-loop "Follow PROMPT.md" --max-iterations {max_iter} --completion-promise "ALL_TASKS_COMPLETE"')


if __name__ == "__main__":
    main()
