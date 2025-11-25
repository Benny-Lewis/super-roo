# Skill Dependencies and Composition Patterns

## Composition Graph

```
using-superpowers (entry point)
├─→ test-driven-development
│   └─→ requesting-code-review
│       └─→ (returns to parent)
├─→ systematic-debugging
│   └─→ requesting-code-review
│       └─→ (returns to parent)
├─→ brainstorming
│   └─→ writing-plans
│       └─→ executing-plans
│           ├─→ test-driven-development (per task)
│           │   └─→ requesting-code-review
│           └─→ (all tasks complete)
├─→ dispatching-parallel-agents
│   ├─→ systematic-debugging (parallel #1)
│   ├─→ systematic-debugging (parallel #2)
│   ├─→ systematic-debugging (parallel #3)
│   └─→ requesting-code-review (after all complete)
└─→ (any of 20 skills based on request)
```

## Primary Composition Patterns

### Pattern 1: TDD with Auto-Review
```
test-driven-development
  (implements using RED-GREEN-REFACTOR)
  → requesting-code-review (AUTOMATIC after GREEN+refactor)
  → (returns feedback)
  → test-driven-development (addresses feedback)
  → verification-before-completion
```

### Pattern 2: Systematic Debugging
```
systematic-debugging
  (4-phase framework)
  → root-cause-tracing (if needed for deep investigation)
  → test-driven-development (to fix with TDD)
  → requesting-code-review (AUTOMATIC after fix)
  → verification-before-completion
```

### Pattern 3: Design → Implementation
```
brainstorming
  (refines design)
  → writing-plans (offers after design approved)
  → executing-plans (offers after plan complete)
    → subagent-driven-development
      → test-driven-development (per task)
        → requesting-code-review
```

### Pattern 4: Parallel Investigations
```
dispatching-parallel-agents
  → systematic-debugging (agent 1)
  → systematic-debugging (agent 2)
  → systematic-debugging (agent 3)
  (all run concurrently with isolated contexts)
  → requesting-code-review (after integration)
```

### Pattern 5: Review Feedback Loop
```
requesting-code-review
  (performs review)
  → (returns feedback to parent)
parent mode
  → receiving-code-review
    → test-driven-development (fix each issue)
      → verification-before-completion
    → requesting-code-review (re-review)
```

## Skill-by-Skill Composition

### Entry Point
- **using-superpowers** → Any skill based on request

### Development Skills
- **test-driven-development** → requesting-code-review (auto)
- **testing-anti-patterns** → (embedded knowledge, no spawning)
- **verification-before-completion** → (terminal, returns evidence)
- **condition-based-waiting** → (embedded knowledge, no spawning)
- **defense-in-depth** → (embedded knowledge, no spawning)
- **receiving-code-review** → test-driven-development (per fix), verification-before-completion
- **requesting-code-review** → (terminal, returns feedback)

### Debugging Skills
- **systematic-debugging** → root-cause-tracing (optional), test-driven-development, requesting-code-review (auto)
- **root-cause-tracing** → (terminal, returns trace info)
- **dispatching-parallel-agents** → systematic-debugging (multiple), requesting-code-review

### Planning & Architecture Skills
- **brainstorming** → writing-plans (offers)
- **writing-plans** → executing-plans (offers)
- **executing-plans** → test-driven-development (per task) OR subagent-driven-development
- **subagent-driven-development** → test-driven-development (per task)
- **using-git-worktrees** → (setup only, no spawning)
- **finishing-a-development-branch** → verification-before-completion, (offers merge/PR options)

### Meta & Workflow Skills
- **writing-skills** → testing-skills-with-subagents (to validate), sharing-skills (to contribute)
- **testing-skills-with-subagents** → Any skill being tested
- **sharing-skills** → using-git-worktrees (optional), receiving-code-review (for PR feedback)

## Auto-Trigger vs. Optional Composition

### AUTOMATIC (no permission)
- test-driven-development → requesting-code-review (after GREEN+refactor)
- systematic-debugging → requesting-code-review (after fix)

### OFFERED (ask user)
- brainstorming → writing-plans
- writing-plans → executing-plans
- finishing-a-development-branch → merge/PR options

### ON-DEMAND (user decides when)
- using-superpowers → any skill
- dispatching-parallel-agents → systematic-debugging
- receiving-code-review → test-driven-development

## Skill Isolation Levels

### TERMINAL (returns without spawning)
- requesting-code-review (returns feedback)
- verification-before-completion (returns evidence)
- root-cause-tracing (returns trace)

### EMBEDDED KNOWLEDGE (no subtasks)
- testing-anti-patterns (guides decisions)
- condition-based-waiting (guides test writing)
- defense-in-depth (guides validation)

### ORCHESTRATORS (spawn multiple)
- using-superpowers (entry point)
- dispatching-parallel-agents (parallel spawning)
- executing-plans (sequential spawning)
- subagent-driven-development (per-task spawning)

### WORKERS (do the work)
- test-driven-development (implements)
- systematic-debugging (investigates)
- brainstorming (designs)
- writing-plans (plans)

## Next Steps

This dependency map will guide:
1. ✅ Mode definition creation (which skills need new_task calls)
2. ✅ Testing strategy (which flows to test)
3. ✅ Documentation (workflow examples)
