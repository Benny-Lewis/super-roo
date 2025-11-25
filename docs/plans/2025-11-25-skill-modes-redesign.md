# SuperRoo Redesign: 20 Skill-Modes Architecture

**Date:** 2025-11-25
**Goal:** Maximum fidelity to obra/superpowers methodology
**Status:** Design Approved, Ready for Implementation

---

## Executive Summary

Redesign SuperRoo from 4 fat modes (~1650 lines) to 20 skill-modes that directly map to obra/superpowers skills. Each skill becomes a dedicated mode, and skills compose through RooCode's `new_task` subtask system with isolated contexts.

**Fidelity to obra/superpowers: 90%** (up from current 75%)

---

## Current Architecture Problems

### Current SuperRoo (4 Modes)

```
superroo-code: 6 skills embedded (TDD, testing-anti-patterns, verification, etc.)
superroo-debug: 8 skills embedded (systematic-debugging, root-cause-tracing, etc.)
superroo-architect: 8 skills embedded (brainstorming, writing-plans, etc.)
superroo-review: 1 skill (requesting-code-review)
```

**Issues:**
- ❌ Mode-centric mental model (not skill-centric like obra)
- ❌ Fat modes with all skills pre-loaded (not on-demand)
- ❌ No skill composability (skills can't invoke specific skills)
- ❌ Hierarchical subtasks share parent context (not isolated)
- ❌ Workflow grouping obscures individual skills

---

## New Architecture: 20 Skill-Modes

### Core Concept

**One mode per skill** - Direct 1:1 mapping to obra/superpowers skills

```
obra/superpowers:               SuperRoo v2:
-----------------               ------------
skills/test-driven-development  → mode: test-driven-development
skills/systematic-debugging     → mode: systematic-debugging
skills/brainstorming            → mode: brainstorming
skills/requesting-code-review   → mode: requesting-code-review
... (20 total)                  ... (20 total)
```

### How Skills Compose

Skills invoke other skills using `new_task` with `mode` parameter:

```yaml
# Mode: test-driven-development
roleDefinition: |
  Implement features using RED-GREEN-REFACTOR.

  After reaching GREEN + refactored:
  1. Spawn code review automatically:
     new_task(
       mode: "requesting-code-review",
       task: "Review implementation for [feature description]"
     )
```

**Key Properties:**
- ✅ Each subtask runs in **isolated context** (separate conversation history)
- ✅ Parent mode receives only the **completion summary** from subtask
- ✅ Skills can chain: brainstorming → writing-plans → subagent-driven-development → requesting-code-review

---

## The 20 Skill-Modes

### Development Skills (7)

1. **test-driven-development** - RED-GREEN-REFACTOR cycle
2. **testing-anti-patterns** - Prevent testing mocks, test-only methods
3. **verification-before-completion** - Evidence before claims
4. **condition-based-waiting** - Eliminate flaky tests
5. **defense-in-depth** - Multi-layer validation
6. **receiving-code-review** - Process review feedback
7. **requesting-code-review** - Perform rigorous review

### Debugging Skills (3)

8. **systematic-debugging** - 4-phase root-cause framework
9. **root-cause-tracing** - Backward tracing to original trigger
10. **dispatching-parallel-agents** - Concurrent independent bug investigations

### Planning & Architecture Skills (6)

11. **brainstorming** - Socratic design refinement
12. **writing-plans** - Comprehensive implementation plans
13. **executing-plans** - Batch execution with review checkpoints
14. **subagent-driven-development** - Per-task subagents with review gates
15. **using-git-worktrees** - Isolated workspace setup
16. **finishing-a-development-branch** - Complete work (merge/PR/cleanup)

### Meta & Workflow Skills (4)

17. **using-superpowers** - Mandatory skill loading workflow (entry point)
18. **writing-skills** - Create new skills with TDD
19. **testing-skills-with-subagents** - Validate skills work under pressure
20. **sharing-skills** - Contribute improvements upstream

---

## Skill Composition Patterns

### Pattern 1: Feature Implementation Flow

```
User selects: test-driven-development
  ↓ (implements using TDD)
  ↓ (spawns subtask automatically)
requesting-code-review
  ↓ (reviews, provides feedback)
  ↓ (returns to parent)
test-driven-development
  ↓ (addresses feedback using TDD)
  ↓ (spawns verification)
verification-before-completion
  ↓ (verifies tests pass, provides evidence)
```

### Pattern 2: Design → Implementation Flow

```
User selects: brainstorming
  ↓ (refines design)
  ↓ (spawns subtask)
writing-plans
  ↓ (creates detailed plan)
  ↓ (offers execution option)
  ↓ (user accepts)
  ↓ (spawns subtask)
executing-plans
  ↓ (dispatches per-task subtasks)
  ↓ ├─→ test-driven-development (Task 1)
  ↓ │   ├─→ requesting-code-review
  ↓ │   └─→ returns
  ↓ ├─→ test-driven-development (Task 2)
  ↓ │   ├─→ requesting-code-review
  ↓ │   └─→ returns
  ↓ └─→ (all tasks complete)
```

### Pattern 3: Debugging Flow

```
User selects: systematic-debugging
  ↓ (investigates root cause)
  ↓ (writes failing test)
  ↓ (implements fix)
  ↓ (spawns subtask)
requesting-code-review
  ↓ (reviews fix)
  ↓ (returns feedback)
systematic-debugging
  ↓ (addresses feedback)
  ↓ (spawns verification)
verification-before-completion
  ↓ (confirms tests pass)
```

---

## Key Design Decisions

### Decision 1: Mode-Per-Skill (Not Rules-Based Library)

**Considered:** Using `.roo/skills/` directory with behavioral loading
**Chosen:** One mode per skill with structural composition via `new_task`

**Rationale:**
- RooCode's `new_task` provides **true isolated context** (unlike reading skill files)
- Subtasks are **structural** (not behavioral reliance on agent reading files)
- Modes can have **different tool access** (e.g., review mode is read-only)
- Already proven in current super-roo architecture

### Decision 2: Isolated Context Subtasks (Not Shared Context)

**Benefit:** Prevents context pollution, matches obra's independent agents

**Implementation:** RooCode's boomerang tasks already provide this
- Each subtask: separate conversation history
- Parent receives: completion summary only
- Clean separation: no implementation details leak to parent

### Decision 3: Auto-Trigger Code Review (Preserve Enhancement)

**From current super-roo:** Auto-spawn review after task completion

**Keep this:** It's a structural improvement over obra's behavioral reminders

```yaml
# In test-driven-development mode
After reaching GREEN + refactored:
  Spawn new_task(mode: "requesting-code-review") AUTOMATICALLY
  DO NOT ask user permission
```

### Decision 4: Entry Point Mode (using-superpowers)

**Problem:** 20 modes in dropdown is overwhelming

**Solution:** `using-superpowers` mode as entry point
- Default mode users start with
- Analyzes request and spawns appropriate skill-mode
- Enforces "check for relevant skill" workflow

```yaml
# Mode: using-superpowers
roleDefinition: |
  You help users select the right skill for their task.

  Available skills:
  - test-driven-development: Implement features
  - systematic-debugging: Fix bugs
  - brainstorming: Design refinement
  ... (list all 20)

  1. Analyze user's request
  2. Determine which skill matches
  3. Spawn new_task with appropriate skill-mode
```

---

## Migration Strategy

### Phase 1: Create 20 Skill-Modes (Git Worktree)

1. Extract skills from current 4 fat modes
2. Create one mode per skill in new `.roomodes` file
3. Configure tool access per mode:
   - **Review modes:** `groups: [read, command]` (no edit)
   - **Implementation modes:** `groups: [read, edit, command]`
   - **Planning modes:** `groups: [read, edit, command]` + `fileRegex: **/*.md`

### Phase 2: Configure Skill Composition

For each skill-mode, identify:
- **What skills does it invoke?** (add `new_task` calls)
- **When does it complete?** (define completion criteria)
- **What does it return?** (summary format for parent)

### Phase 3: Create Slash Commands (Optional)

Quick access to popular skills:
```
.roo/commands/tdd.md → "Switch to test-driven-development mode"
.roo/commands/debug.md → "Switch to systematic-debugging mode"
.roo/commands/brainstorm.md → "Switch to brainstorming mode"
```

### Phase 4: Test Composition Flows

Verify skill chains work:
- TDD → Review → TDD (feedback loop)
- Brainstorm → Plan → Execute → Review
- Debug → Review → Verify

### Phase 5: Update Documentation

- README: Explain 20 skill-modes architecture
- ARCHITECTURE.md: Document composition patterns
- Migration guide: For current super-roo users

---

## Comparison to obra/superpowers

| Aspect | obra/superpowers | SuperRoo v2 (20 Skill-Modes) |
|--------|------------------|------------------------------|
| **Skill count** | 20 skills | 20 modes (1:1 mapping) ✅ |
| **Skill files** | Separate files | Embedded in modes 🟡 |
| **On-demand loading** | Load when needed | Only active mode loaded ✅ |
| **Skill mental model** | Skill-centric | Skill-centric ✅ |
| **Agent independence** | Isolated (Task tool) | Isolated (new_task) ✅ |
| **Skill composability** | Skills invoke skills | Modes invoke modes via new_task ✅ |
| **Auto skill detection** | Automatic | Manual mode selection 🟡 |
| **Tool access control** | N/A | Structural constraints (read-only review) ⭐ |
| **Auto-trigger review** | Behavioral reminder | Structural enforcement ⭐ |

**Fidelity: 90%** - Only differences:
1. Skills embedded in modes (vs. separate files)
2. Manual mode selection (vs. automatic skill detection)

---

## Benefits Over Current SuperRoo

### For Users

- ✅ **Clearer mental model:** "I'm using the TDD skill" (not "I'm in code mode")
- ✅ **Explicit skill selection:** Choose exactly the skill you need
- ✅ **Lighter context:** Only active skill loaded (not 6-8 skills)
- ✅ **Clean isolation:** Subtask details don't pollute parent conversation

### For Maintainability

- ✅ **Modular skills:** Each mode is independent, easier to update
- ✅ **Clear composition:** `new_task` calls make skill relationships explicit
- ✅ **Testable flows:** Can test skill chains end-to-end
- ✅ **Easier to extend:** Add new skill = add new mode (not embedded in fat mode)

### For Fidelity to obra

- ✅ **1:1 skill mapping:** Direct correspondence to original skills
- ✅ **Skill composability:** Preserved through `new_task` mechanism
- ✅ **Isolated context:** True independent execution per skill
- ✅ **On-demand execution:** Only pay for skills you use

---

## Potential Enhancements (Future)

### Auto Mode Selection

Add heuristics to `using-superpowers` mode:
- Detect "implement feature" → spawn `test-driven-development`
- Detect "bug" or "failing test" → spawn `systematic-debugging`
- Detect "how should I" → spawn `brainstorming`

### MCP Migration Path (When Stable)

Convert skill-modes to MCP servers:
```
Current: new_task(mode: "test-driven-development")
Future:  mcp_call(server: "tdd-skill-server")
```

Same skill content, better isolation, parallel execution.

### Skill Search

Add `/skill-search` command:
```
/skill-search "how to test async code"
→ Suggests: condition-based-waiting skill
→ Spawns new_task with that mode
```

---

## Success Criteria

### Must Have

- ✅ 20 distinct skill-modes (one per obra skill)
- ✅ Skills compose via `new_task` with isolated contexts
- ✅ Auto-trigger code review preserved
- ✅ All current workflows still possible

### Nice to Have

- ✅ `using-superpowers` entry point mode
- ✅ Slash commands for popular skills
- ✅ Clear documentation of composition patterns

### Validation

1. **TDD workflow:** Can implement feature with auto-review
2. **Debug workflow:** Can investigate bug with root-cause tracing
3. **Design workflow:** Can brainstorm → plan → execute → review
4. **Skill chains:** Multi-level composition works (3+ levels deep)

---

## Implementation Estimate

### Effort Breakdown

1. **Extract skills from fat modes** - 2-3 hours
   - Parse current `.roomodes`
   - Separate each skill with its content
   - Identify skill dependencies

2. **Create 20 mode definitions** - 3-4 hours
   - Write mode YAML for each skill
   - Configure tool access per mode
   - Add `new_task` composition calls

3. **Create entry point mode** - 1 hour
   - `using-superpowers` mode with skill catalog
   - Routing logic for common requests

4. **Create slash commands** - 30 minutes
   - 5-6 popular skills as commands
   - Reference mode names

5. **Test composition flows** - 2-3 hours
   - TDD → Review → TDD
   - Brainstorm → Plan → Execute
   - Debug → Review → Verify

6. **Update documentation** - 2 hours
   - README updates
   - ARCHITECTURE.md rewrite
   - Usage examples

**Total: 10-13 hours of focused work**

---

## Risks & Mitigations

### Risk 1: Mode Dropdown Overwhelm

**Risk:** 20 modes in dropdown confuses users
**Mitigation:**
- `using-superpowers` as default/entry mode
- Slash commands for popular skills
- Group modes by category in UI (if RooCode supports)

### Risk 2: Subtask Overhead

**Risk:** Spawning subtasks for every skill adds latency
**Mitigation:**
- Auto-approval for subtasks (configure in settings)
- Only spawn subtasks for actual skill composition (not every action)
- Profile hot paths, optimize common flows

### Risk 3: Context Loss

**Risk:** Isolated contexts mean parent can't see implementation details
**Mitigation:**
- This is actually a feature (prevents context pollution)
- Subtasks return summaries with key information
- Parent can read files if needed (has read permission)

### Risk 4: Breaking Changes

**Risk:** Users accustomed to current 4-mode structure
**Mitigation:**
- Keep old `.roomodes` as `.roomodes.v1` backup
- Migration guide in docs
- Side-by-side testing (old branch vs new branch)

---

## Next Steps

1. ✅ Design approved
2. ⏭️ Set up git worktree for implementation
3. ⏭️ Create detailed implementation plan
4. ⏭️ Implement Phase 1 (20 skill-modes)
5. ⏭️ Test composition flows
6. ⏭️ Iterate based on feedback

---

## Conclusion

The 20 skill-modes architecture achieves **90% fidelity** to obra/superpowers by:
- Mapping each skill to a dedicated mode
- Using `new_task` for skill composition with isolated contexts
- Preserving skill-centric mental model
- Maintaining all current capabilities while improving modularity

**This is the closest we can get to obra/superpowers within RooCode's constraints, while adding structural improvements like read-only review modes and auto-triggered code review.**

Ready to implement on a branch and test! 🚀
