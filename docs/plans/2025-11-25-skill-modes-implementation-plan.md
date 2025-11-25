# Implementation Plan: 20 Skill-Modes Architecture

**Branch:** `skill-modes-redesign`
**Worktree:** `/mnt/c/users/blewis/dev/super-roo-skill-modes`
**Date:** 2025-11-25

---

## Overview

Transform SuperRoo from 4 fat modes to 20 skill-modes for maximum fidelity to obra/superpowers.

**Total Effort:** 10-13 hours
**Approach:** Incremental, testable phases

---

## Phase 1: Extract Skills from Current Modes (2-3 hours)

### Task 1.1: Analyze Current .roomodes Structure

**Goal:** Understand what skills are embedded in each mode

**Steps:**
1. Read current `.roomodes` file
2. Identify skill boundaries within each mode
3. Document which skills are in which modes:
   - superroo-code: TDD, testing-anti-patterns, verification, requesting-code-review, condition-based-waiting, defense-in-depth
   - superroo-debug: systematic-debugging, root-cause-tracing, TDD, testing-anti-patterns, verification, requesting-code-review, condition-based-waiting, defense-in-depth
   - superroo-architect: brainstorming, writing-plans, executing-plans, using-git-worktrees, finishing-a-development-branch, subagent-driven-development, verification, requesting-code-review
   - superroo-review: requesting-code-review

**Verification:** List of 20 skills with their current locations

### Task 1.2: Extract Skill Content

**Goal:** Separate each skill into standalone content

**Steps:**
1. Create `work/skills/` directory for extracted content
2. For each skill, extract:
   - Skill name
   - Skill description
   - Skill instructions (full content)
   - When to use guidance
   - Tool requirements (read/edit/command)
3. Save each skill as `work/skills/{skill-name}.md`

**Verification:** 20 markdown files in `work/skills/` directory

### Task 1.3: Identify Skill Dependencies

**Goal:** Map which skills invoke other skills

**Steps:**
1. For each skill, identify references to other skills
2. Document skill composition patterns:
   ```
   test-driven-development → requesting-code-review
   systematic-debugging → requesting-code-review
   brainstorming → writing-plans
   writing-plans → executing-plans
   executing-plans → test-driven-development (per task)
   ```
3. Create dependency graph in `work/skill-dependencies.md`

**Verification:** Dependency graph showing all skill relationships

---

## Phase 2: Create 20 Skill-Mode Definitions (3-4 hours)

### Task 2.1: Define Mode Template

**Goal:** Standardize mode structure across all skills

**Template:**
```yaml
- slug: {skill-name}
  name: {Skill Display Name}
  description: "{Short description}"
  roleDefinition: |
    # SKILL: {SKILL NAME}

    {Skill instructions from extracted content}

    ## SKILL COMPLETION

    This skill completes when: {completion criteria}

    Return to parent task with summary: {what to include}

    ## SKILL COMPOSITION

    When this skill needs other skills:
    - {Other skill}: new_task(mode: "{other-skill-slug}", task: "{description}")

    ## COMMUNICATION AND TOOL USAGE

    ALWAYS communicate before using tools:
    - Explain what you're about to do
    - Use tools
    - Explain results
  whenToUse: |
    {When to use guidance from extracted content}
  groups:
    - {read/edit/command based on skill needs}
```

**Verification:** Template document created

### Task 2.2: Create Development Skill Modes (7 modes)

**Skills to convert:**
1. test-driven-development
2. testing-anti-patterns
3. verification-before-completion
4. condition-based-waiting
5. defense-in-depth
6. receiving-code-review
7. requesting-code-review

**For each skill:**
1. Use template from Task 2.1
2. Fill in skill-specific content from `work/skills/{skill}.md`
3. Configure tool access:
   - Most: `groups: [read, edit, command]`
   - requesting-code-review: `groups: [read, command]` (read-only)
4. Add `new_task` composition calls:
   - test-driven-development → requesting-code-review (after GREEN+refactor)
   - requesting-code-review → returns feedback to parent
5. Define completion criteria
6. Add to new `.roomodes` file

**Verification:** 7 mode definitions in `.roomodes`, each properly configured

### Task 2.3: Create Debugging Skill Modes (3 modes)

**Skills to convert:**
8. systematic-debugging
9. root-cause-tracing
10. dispatching-parallel-agents

**For each skill:**
1. Use template
2. Fill in content
3. Configure: `groups: [read, edit, command]`
4. Add composition:
   - systematic-debugging → requesting-code-review (after fix)
   - root-cause-tracing → returns to systematic-debugging
   - dispatching-parallel-agents → spawns multiple systematic-debugging subtasks
5. Add to `.roomodes`

**Verification:** 3 more modes added (10 total)

### Task 2.4: Create Planning Skill Modes (6 modes)

**Skills to convert:**
11. brainstorming
12. writing-plans
13. executing-plans
14. subagent-driven-development
15. using-git-worktrees
16. finishing-a-development-branch

**For each skill:**
1. Use template
2. Fill in content
3. Configure tool access:
   - brainstorming: `groups: [read, edit, command]` + `fileRegex: **/*.md`
   - writing-plans: `groups: [read, edit, command]` + `fileRegex: **/*.md`
   - Others: `groups: [read, edit, command]`
4. Add composition:
   - brainstorming → writing-plans (after design approved)
   - writing-plans → executing-plans (if user wants execution)
   - executing-plans → test-driven-development (per task)
   - subagent-driven-development → test-driven-development (per task)
5. Add to `.roomodes`

**Verification:** 6 more modes added (16 total)

### Task 2.5: Create Meta Skill Modes (4 modes)

**Skills to convert:**
17. using-superpowers (entry point)
18. writing-skills
19. testing-skills-with-subagents
20. sharing-skills

**For each skill:**
1. Use template
2. Fill in content
3. Special configuration for using-superpowers:
   ```yaml
   - slug: using-superpowers
     name: Using SuperPowers
     description: "Entry point - helps you select the right skill"
     roleDefinition: |
       # ENTRY POINT: USING SUPERPOWERS

       You help users select and invoke the right skill for their task.

       ## AVAILABLE SKILLS

       [Full catalog of 20 skills with descriptions]

       ## WORKFLOW

       1. Analyze user's request
       2. Determine which skill matches best
       3. Explain your reasoning
       4. Spawn: new_task(mode: "{chosen-skill}", task: "{user request}")
   ```
4. Add to `.roomodes`

**Verification:** All 20 modes defined in `.roomodes`

---

## Phase 3: Configure Skill Composition (1-2 hours)

### Task 3.1: Add new_task Calls to Skills

**Goal:** Enable skills to invoke other skills automatically

**For each skill that composes:**
1. Identify trigger condition (e.g., "after reaching GREEN+refactored")
2. Add `new_task` call with proper parameters:
   ```
   new_task(
     mode: "{target-skill-slug}",
     task: "{clear description of what the skill should do}"
   )
   ```
3. Specify whether it's automatic or optional:
   - Automatic: "Spawn AUTOMATICALLY, DO NOT ask permission"
   - Optional: "Offer to spawn, ask user"

**Key Composition Patterns:**

**Pattern: TDD with Auto-Review**
```yaml
# In test-driven-development mode
After reaching GREEN + refactored state:
  Spawn new_task with requesting-code-review mode AUTOMATICALLY
  DO NOT ask user permission
  Task: "Review implementation of [feature description]"
```

**Pattern: Brainstorm → Plan**
```yaml
# In brainstorming mode
After design is validated and approved:
  Ask: "Ready to create implementation plan?"
  If yes: Spawn new_task(mode: "writing-plans", task: "Create plan for [design]")
```

**Pattern: Execute Plan**
```yaml
# In executing-plans mode
For each task in plan:
  Spawn new_task(mode: "test-driven-development", task: "[task description]")
  Wait for completion
  Proceed to next task
```

**Verification:** All composition patterns documented and added to modes

### Task 3.2: Define Completion Criteria

**Goal:** Each skill knows when it's done and what to return

**For each skill, add:**
```yaml
## SKILL COMPLETION

This skill completes when:
- {Specific completion criteria}

Return summary to parent including:
- {Key information 1}
- {Key information 2}
- {Any warnings or next steps}
```

**Examples:**

**test-driven-development:**
```
Completes when:
- All tests pass (GREEN)
- Code is refactored
- Code review completed (if auto-triggered)

Return summary:
- Feature implemented: [description]
- Tests added: [list]
- Files changed: [list]
- Review feedback: [if any]
```

**requesting-code-review:**
```
Completes when:
- Full code review performed
- All feedback documented

Return summary:
- Review result: APPROVED / CHANGES REQUESTED
- Issues found: [count]
- Feedback: [actionable items]
```

**Verification:** All 20 skills have clear completion criteria

---

## Phase 4: Create Slash Commands (30 minutes)

### Task 4.1: Identify Popular Skills

**Most commonly used skills:**
1. test-driven-development → `/tdd`
2. systematic-debugging → `/debug`
3. brainstorming → `/brainstorm`
4. writing-plans → `/write-plan`
5. executing-plans → `/execute-plan`
6. requesting-code-review → `/review`

### Task 4.2: Create Command Files

**For each command:**
1. Create `.roo/commands/{command-name}.md`
2. Content:
   ```markdown
   ---
   description: {Description of what this skill does}
   ---

   Switch to {skill-name} mode and apply its methodology.
   ```

**Example:** `.roo/commands/tdd.md`
```markdown
---
description: Implement features using test-driven development
---

Switch to test-driven-development mode and use RED-GREEN-REFACTOR cycle.
```

**Verification:** 6 slash command files created

---

## Phase 5: Test Composition Flows (2-3 hours)

### Task 5.1: Test TDD → Review → TDD Flow

**Scenario:** Implement simple feature with auto-review

**Steps:**
1. Start in `using-superpowers` mode
2. Request: "Implement a function that checks if a number is prime"
3. Verify: Spawns `test-driven-development` mode
4. Verify: Follows RED-GREEN-REFACTOR
5. Verify: Auto-spawns `requesting-code-review`
6. Verify: Returns feedback to TDD mode
7. Verify: TDD mode addresses feedback

**Success Criteria:**
- ✅ Automatic mode selection works
- ✅ Subtask has isolated context
- ✅ Auto-trigger review works
- ✅ Feedback loop works

### Task 5.2: Test Brainstorm → Plan → Execute Flow

**Scenario:** Design and implement a feature

**Steps:**
1. Start in `brainstorming` mode
2. Request: "I want to add caching"
3. Verify: Asks clarifying questions
4. Verify: Proposes 2-3 approaches
5. Verify: Presents design incrementally
6. Verify: Offers to create plan
7. User accepts
8. Verify: Spawns `writing-plans` mode
9. Verify: Creates detailed plan
10. Verify: Offers execution
11. User accepts
12. Verify: Spawns `executing-plans` mode
13. Verify: Executes tasks one by one via TDD subtasks

**Success Criteria:**
- ✅ Multi-level composition works (3+ levels deep)
- ✅ Each level has isolated context
- ✅ Summaries flow back up correctly

### Task 5.3: Test Debug → Review Flow

**Scenario:** Fix a bug with systematic debugging

**Steps:**
1. Start in `systematic-debugging` mode
2. Request: "Tests failing: empty email accepted"
3. Verify: Follows 4-phase framework
4. Verify: Creates failing test (RED)
5. Verify: Implements fix (GREEN)
6. Verify: Auto-spawns `requesting-code-review`
7. Verify: Review provides feedback
8. Verify: Debug mode addresses feedback

**Success Criteria:**
- ✅ Debugging workflow preserved
- ✅ Auto-review works
- ✅ Feedback loop works

### Task 5.4: Test Parallel Agents

**Scenario:** Multiple independent bugs

**Steps:**
1. Start in `dispatching-parallel-agents` mode
2. Request: "Fix these 3 bugs: [list]"
3. Verify: Spawns 3 `systematic-debugging` subtasks
4. Verify: Each runs independently
5. Verify: All complete and return summaries

**Success Criteria:**
- ✅ Can spawn multiple subtasks
- ✅ Subtasks run independently
- ✅ Parent coordinates completion

---

## Phase 6: Update Documentation (2 hours)

### Task 6.1: Update README.md

**Changes needed:**
1. Replace "4 Custom Modes" with "20 Skill-Modes"
2. Update architecture summary:
   ```markdown
   ## What You Get

   **20 Skill-Modes** (1:1 mapping to obra/superpowers skills):
   - One mode per skill for clarity and focus
   - Skills compose via subtasks with isolated contexts
   - Entry point mode helps you select the right skill
   ```
3. Update Quick Start:
   ```markdown
   ### Quick Start

   1. **Start with using-superpowers mode** - Entry point that helps you select the right skill
   2. **Or use slash commands** - Quick access: `/tdd`, `/debug`, `/brainstorm`
   3. **Skills auto-compose** - TDD automatically triggers review, brainstorm offers to create plan
   4. **Each skill runs isolated** - Clean context separation, summaries flow back to parent
   ```
4. Update workflow example with 20 skill-modes
5. Update installation instructions (same files, different structure)

**Verification:** README accurately describes new architecture

### Task 6.2: Update ARCHITECTURE.md

**Changes needed:**
1. Update architecture comparison table:
   ```markdown
   | Aspect | Original Superpowers | SuperRoo v2 (20 Skill-Modes) |
   |--------|---------------------|------------------------------|
   | Unit of work | Skills (20 files) | Modes (20 modes) |
   | Subtasks | Independent (Task tool) | Isolated (new_task) |
   | Fidelity | 100% (reference) | 90% |
   ```
2. Replace "4 Custom Modes" section with "20 Skill-Modes" section
3. Document each of the 20 modes with:
   - Purpose
   - Tool access
   - Composition patterns
   - Completion criteria
4. Update workflow examples
5. Update "Key Design Decisions" section
6. Add new section: "Skill Composition Patterns"

**Verification:** ARCHITECTURE.md accurately documents new design

### Task 6.3: Create Migration Guide

**Create:** `docs/MIGRATION.md`

**Content:**
1. Why we redesigned (90% fidelity goal)
2. What changed:
   - 4 modes → 20 modes
   - Fat embedded skills → One skill per mode
   - Hierarchical context → Isolated subtasks
3. How to migrate:
   - Install new `.roomodes`
   - Use `using-superpowers` as entry point
   - Or use slash commands for direct access
4. What stayed the same:
   - All workflows still work
   - Auto-trigger review preserved
   - Same core principles
5. Troubleshooting common issues

**Verification:** Clear migration path documented

---

## Validation Checklist

Before merging to main, verify:

### Functionality
- [ ] All 20 skill-modes defined in `.roomodes`
- [ ] `using-superpowers` entry point works
- [ ] Slash commands work
- [ ] Skills can spawn other skills via `new_task`
- [ ] Subtasks have isolated contexts
- [ ] Auto-trigger code review works
- [ ] Multi-level composition works (3+ levels)

### Documentation
- [ ] README.md updated
- [ ] ARCHITECTURE.md updated
- [ ] MIGRATION.md created
- [ ] All workflow examples updated

### Testing
- [ ] TDD → Review → TDD flow works
- [ ] Brainstorm → Plan → Execute flow works
- [ ] Debug → Review flow works
- [ ] Parallel agents flow works

### Quality
- [ ] No syntax errors in `.roomodes`
- [ ] All mode slugs follow naming convention
- [ ] All tool access properly configured
- [ ] All composition patterns documented

---

## Rollback Plan

If issues arise:

1. **Keep old version:** Original `.roomodes` backed up as `.roomodes.v1`
2. **Easy revert:** `cp .roomodes.v1 .roomodes && git checkout main`
3. **Side-by-side testing:** Both worktrees available during transition

---

## Next Steps After Implementation

1. **Test in real projects** - Use for actual development work
2. **Gather feedback** - What works? What's confusing?
3. **Iterate** - Adjust skill definitions based on usage
4. **Consider enhancements:**
   - Auto mode selection heuristics
   - Skill search functionality
   - MCP migration path (when stable)

---

## Summary

This plan transforms SuperRoo into a 90% faithful port of obra/superpowers by:
- Creating 20 skill-modes (1:1 skill mapping)
- Enabling skill composition via `new_task` with isolated contexts
- Preserving all current capabilities while improving fidelity
- Providing clear migration path and documentation

**Estimated total time: 10-13 hours**

Ready to implement! 🚀
