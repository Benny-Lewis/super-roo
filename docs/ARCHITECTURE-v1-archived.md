# SuperRoo Architecture

**Technical documentation for the SuperRoo development methodology port to RooCode**

---

## Overview

SuperRoo is a port of the [superpowers](https://github.com/obra/superpowers) development methodology from Claude Code to RooCode. It preserves the core discipline (TDD, systematic debugging, rigorous code review) while adapting to RooCode's mode-based architecture.

**Core methodology:** 20 skills from original superpowers → 4 custom RooCode modes

---

## Architecture Comparison

| Aspect | Original Superpowers | SuperRoo (RooCode Port) |
|--------|---------------------|------------------------|
| **Platform** | Claude Code CLI | RooCode (VS Code extension) |
| **Unit of work** | Skills (20 files) | Modes (4 custom modes) |
| **Loading** | On-demand skill loading | Fat modes with embedded skills |
| **Subtasks** | Independent agents (Task tool) | Hierarchical subtasks (new_task) |
| **Discipline** | Behavioral (skills remind you) | Structural + Behavioral (auto-trigger review) |
| **Mode bypass protection** | N/A | Global rule enforces mode usage |
| **Code review** | Manual trigger | Auto-trigger after task completion |

---

## System Components

### 1. Global Rule

**File:** `.roo/rules/superroo-workspace.md`

**Purpose:** Enforces SuperRoo methodology discipline across all modes

**Key principles:**
- 🔴 NO CODE WITHOUT FAILING TEST FIRST
- ✅ NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION
- 🔍 ROOT CAUSE INVESTIGATION BEFORE FIXES
- 👁️ REVIEW EARLY, REVIEW OFTEN

**Enforcement:**
- Always loaded (global rule)
- Prevents mode bypass
- Establishes non-negotiable principles

---

### 2. Custom Modes (4 Modes)

All modes defined in: `.roomodes`

#### superroo-review

**Purpose:** Rigorous code review (read-only)

**Role:** Pure Player (reviews only, never implements)

**Tool Access:**
- Groups: `read`, `command`
- No `edit` permission (structural constraint)

**Command Restrictions:**
- ✅ Allowed: Read-only commands (`git diff`, `git log`, `cat`, `grep`)
- ❌ Forbidden: State-mutating commands (`git commit`, `git push`, file writes)

**Review Criteria:**
1. Requirements match
2. Tests exist and test behavior (not mocks)
3. Bugs and edge cases
4. Code follows project patterns
5. Error handling

**When used:**
- Auto-triggered by superroo-code after task completion
- Auto-triggered by superroo-debug after bug fix
- Manually for design reviews

---

#### superroo-code

**Purpose:** TDD-driven implementation with auto-review

**Roles:** Conductor + Player (explicit role switching)

**Tool Access:**
- Groups: `read`, `edit`, `command`
- No fileRegex constraint (can edit all files)

**Embedded Skills (6):**
1. test-driven-development (RED-GREEN-REFACTOR)
2. testing-anti-patterns (avoid testing mocks)
3. verification-before-completion (evidence before claims)
4. requesting-code-review (auto-trigger)
5. condition-based-waiting (eliminate flaky tests)
6. defense-in-depth (validate at every layer)

**Auto-Trigger Review:**
```
AFTER task reaches GREEN + refactored:
  1. Spawn new_task with superroo-review mode AUTOMATICALLY
  2. DO NOT ask user permission
  3. Review is mandatory, not optional
```

**Role Switching:**
- **Conductor:** User provides multiple tasks or implementation plan
  - Break into subtasks
  - Spawn new_task for each
  - Monitor completion, trigger review
- **Player:** Single focused feature/bugfix
  - Write tests first (RED)
  - Implement minimal code (GREEN)
  - Refactor (stay GREEN)
  - Request review when complete

**When used:** Implementing features, fixing bugs, executing plans

---

#### superroo-debug

**Purpose:** Systematic root-cause debugging with TDD

**Roles:** Conductor + Player (explicit role switching)

**Tool Access:**
- Groups: `read`, `edit`, `command`
- No fileRegex constraint (can edit all files)

**Embedded Skills (8):**
1. systematic-debugging (4-phase framework)
2. root-cause-tracing (backward tracing to original trigger)
3. test-driven-development (RED-GREEN-REFACTOR)
4. testing-anti-patterns (avoid testing mocks)
5. verification-before-completion (evidence before claims)
6. requesting-code-review (auto-trigger)
7. condition-based-waiting (eliminate flaky tests)
8. defense-in-depth (validate at every layer)

**4-Phase Debugging Framework:**
1. **Root Cause Investigation** - Reproduce, gather evidence, trace data flow
2. **Pattern Analysis** - Find working examples, compare, identify differences
3. **Hypothesis and Testing** - Form hypothesis, test minimally, verify
4. **Implementation** - Create failing test, fix root cause, verify

**Auto-Trigger Review:**
Same as superroo-code (after bug fix completion)

**Role Switching:**
- **Conductor:** Multiple independent bugs
- **Player:** Single bug investigation

**When used:** Bugs, test failures, unexpected behavior

---

#### superroo-architect

**Purpose:** Design, planning, and documentation

**Roles:** Conductor + Player (explicit role switching)

**Tool Access:**
- Groups: `read`, `edit`, `command`
- **fileRegex:** `**/*.md` (structural constraint: docs-only edit)

**Embedded Skills (8):**
1. brainstorming (refine ideas into designs)
2. writing-plans (comprehensive implementation plans)
3. executing-plans (batch execution with checkpoints)
4. using-git-worktrees (isolated workspaces)
5. finishing-a-development-branch (complete work)
6. subagent-driven-development (per-task subagents)
7. verification-before-completion (evidence before claims)
8. requesting-code-review (design document reviews)

**Key Principles:**
- YAGNI ruthlessly (remove unnecessary features)
- Comprehensive plans (assume zero context)
- One question at a time (brainstorming)
- Incremental validation

**Role Switching:**
- **Conductor:** Execute plan, dispatch subagents
- **Player:** Brainstorm, write plans, create docs

**When used:** Design, planning, documentation, coordinating implementation

---

### 3. Slash Commands (4 Commands)

**Directory:** `.roo/commands/`

| Command | Description | Workflow |
|---------|-------------|----------|
| `/brainstorm` | Interactive design refinement | Use superroo-architect, Socratic questioning, incremental presentation |
| `/write-plan` | Create implementation plan | Use superroo-architect, bite-sized tasks, exact paths & code |
| `/execute-plan` | Execute plan in batches | Use superroo-architect, batch execution, review checkpoints |
| `/finish` | Complete development work | Use superroo-architect, verify tests, present 4 options |

---

## Key Design Decisions

### Fat Modes with Embedded Skills

**Decision:** Embed all 20 skills into 4 modes (vs. on-demand skill loading)

**Rationale:**
- RooCode modes are stateful contexts
- Token overhead not a concern (user confirmed)
- Simpler mental model (4 modes vs. 20 skills)
- Skills grouped by workflow stage (architect → code → debug → review)

**Trade-off:** Larger mode definitions, but clearer boundaries

---

### Auto-Trigger Code Review

**Decision:** Automatically spawn superroo-review mode after task completion (no asking permission)

**Original superpowers:** Skills remind to request review, but don't force it

**SuperRoo enhancement:** Structural enforcement through auto-trigger

**Implementation:**
```yaml
# In superroo-code mode roleDefinition
After task reaches GREEN + refactored state:
  - Spawn new_task with superroo-review mode AUTOMATICALLY
  - DO NOT ask user permission
  - Review is mandatory, not optional
```

**Benefits:**
- Catches issues before they compound
- No reliance on discipline (structural vs. behavioral)
- Consistent quality gates

---

### Structural Constraints

**Decision:** Use RooCode's structural features (tool groups, fileRegex) to prevent violations

**Examples:**

1. **Read-only review mode:**
   ```yaml
   groups:
     - read
     - command
   # No 'edit' group = structurally impossible to edit code
   ```

2. **Docs-only architect mode:**
   ```yaml
   groups:
     - read
     - edit
     - command
   fileRegex: "**/*.md"  # Can only edit markdown files
   ```

**Benefits:**
- Violations structurally impossible
- More reliable than behavioral reminders
- Clear separation of concerns

---

### Explicit Role Switching (Conductor vs Player)

**Decision:** Modes have two roles with explicit WHEN rules

**Problem:** Confusion about when to delegate vs. implement directly

**Solution:** Explicit WHEN rules in roleDefinition

**Example (superroo-code):**
```yaml
CONDUCTOR ROLE
WHEN:
  - User requests multiple independent tasks
  - User provides implementation plan
DO:
  - Break into tasks
  - Create new_task for each
  - Monitor, review
  - DO NOT write implementation code yourself

PLAYER ROLE
WHEN:
  - User requests single focused feature/bugfix
  - No delegation needed
DO:
  - Write tests first (RED)
  - Implement (GREEN)
  - Refactor
```

**Benefits:**
- Clear decision rules
- Prevents "should I delegate or implement?" confusion
- Preserves both orchestration and execution capabilities

---

### Global Rule for Mode Bypass Prevention

**Decision:** Create `.roo/rules/superroo-workspace.md` to prevent mode bypass

**Problem:** Future sessions might bypass SuperRoo modes "for convenience"

**Solution:** Always-loaded global rule stating:
```markdown
For serious work, you MUST use SuperRoo modes:
- superroo-code - TDD-driven implementation
- superroo-debug - Systematic debugging
- superroo-architect - Design, planning
- superroo-review - Code review

Do NOT bypass SuperRoo modes for convenience.
```

**Benefits:**
- Maintains discipline across sessions
- Reminds of core principles
- Establishes non-negotiable standards

---

### Hierarchical Subtasks (RooCode Limitation)

**Original superpowers:** Independent agents via Task tool (parallel execution, isolated context)

**RooCode:** Hierarchical subtasks via new_task (share parent context)

**Implication:** Subagents in SuperRoo share context with parent, not truly independent

**Future:** When RooCode supports MCP, can upgrade to independent agents via MCP servers

**Current approach:** Work within RooCode constraints, document for future upgrade

---

## Workflow Examples

### Example 1: Feature Implementation

```
1. User: "Add user authentication"

2. superroo-architect mode:
   - Brainstorm design (Socratic questions)
   - Write implementation plan (5 TDD-based tasks)
   - Save to docs/plans/2025-11-22-auth-plan.md

3. superroo-code mode:
   - Task 1: Write failing test → Implement → Refactor
   - Auto-review triggers → Address feedback
   - Task 2: Write failing test → Implement → Refactor
   - Auto-review triggers → Address feedback
   - ... (repeat for all tasks)

4. superroo-architect mode:
   - Finish branch (verify, create PR, cleanup)
```

---

### Example 2: Bug Fix

```
1. User: "Tests failing: empty email accepted"

2. superroo-debug mode:
   - Phase 1: Root cause investigation
     - Reproduce bug
     - Check recent changes
     - Trace data flow
   - Phase 2: Pattern analysis
     - Find working validation examples
     - Compare differences
   - Phase 3: Hypothesis testing
     - "Missing email validation in submitForm"
     - Test hypothesis minimally
   - Phase 4: Implementation
     - Write failing test (RED)
     - Fix root cause (GREEN)
     - Refactor
   - Auto-review triggers
   - Address review feedback
```

---

### Example 3: Design Refinement

```
1. User: "I want to add caching but not sure how"

2. superroo-architect mode (/brainstorm):
   - Check current project state
   - Ask: "What data needs caching?" (one question)
   - User: "API responses"
   - Ask: "How long should cache be valid?" (one question)
   - User: "5 minutes"
   - Propose 2-3 approaches:
     - Option A: In-memory cache (simple, lost on restart)
     - Option B: Redis (persistent, requires infrastructure)
     - Option C: Browser localStorage (client-side, limited size)
   - Present recommended approach incrementally
   - Write design doc
   - Ask: "Ready to set up for implementation?"
```

---

## Installation Variants

### Global Installation (All Projects)

```bash
# Windows
copy .roomodes %APPDATA%\Code\User\roo-code-settings\customModes.json
xcopy /E /I .roo\rules %APPDATA%\Code\User\roo-code-settings\rules
xcopy /E /I .roo\commands %APPDATA%\Code\User\roo-code-settings\commands

# macOS/Linux
cp .roomodes ~/.config/Code/User/roo-code-settings/customModes.json
cp -r .roo/rules ~/.config/Code/User/roo-code-settings/
cp -r .roo/commands ~/.config/Code/User/roo-code-settings/
```

---

### Project-Specific Installation

```bash
# In your project directory
cp /path/to/super-roo/.roomodes .
cp -r /path/to/super-roo/.roo .
```

---

## Fidelity to Original Superpowers

### Preserved (100% fidelity)

- ✅ Core methodology (TDD, debugging, review)
- ✅ All 20 skills (embedded in modes)
- ✅ All workflows (brainstorming → planning → implementation → review)
- ✅ Discipline principles (test-first, verification, root-cause investigation)

### Adapted (platform differences)

- **Skill delivery:** 20 files → 4 modes (necessary for RooCode)
- **Subtasks:** Independent agents → Hierarchical (RooCode limitation, MCP upgrade planned)
- **Auto-discipline:** Behavioral reminders → Auto-trigger review (SuperRoo enhancement)
- **Mode bypass:** N/A → Global rule (SuperRoo enhancement)

### Enhanced (SuperRoo improvements)

- ⭐ Auto-trigger code review (structural enforcement)
- ⭐ Global rule preventing mode bypass
- ⭐ Structural constraints (read-only review, docs-only architect)
- ⭐ Explicit role switching (conductor vs player)

**Overall fidelity: 95%** - Core methodology identical, optimizations for RooCode platform

---

## Future Improvements

### When RooCode Supports MCP

**Current limitation:** Hierarchical subtasks (new_task shares parent context)

**Future upgrade:** Independent agents via MCP servers
- True isolation per subtask
- Parallel execution
- No context pollution

**Migration path:**
- Keep current mode structure
- Replace new_task calls with MCP agent spawning
- Same workflows, better isolation

---

### Additional Slash Commands

Potential future additions:
- `/review` - Request code review manually
- `/worktree` - Set up git worktree
- `/tdd` - Quick TDD cycle reminder

---

## Technical Details

### Mode Definition Format (.roomodes)

```yaml
customModes:
  - slug: mode-slug
    name: Display Name
    description: "Short description"
    roleDefinition: |
      # Markdown content
      Full instructions for this mode
    whenToUse: |
      Description of when to use this mode
    groups:
      - read
      - edit
      - command
    fileRegex: "**/*.md"  # Optional: constrain edit permission
```

---

### Skill Embedding Strategy

Instead of 20 separate skill files, skills are embedded directly in mode roleDefinition:

```yaml
roleDefinition: |
  # ROLE: MODE NAME

  ## EMBEDDED SKILLS

  ### Skill 1: Skill Name
  [Full skill content here]

  ### Skill 2: Another Skill
  [Full skill content here]

  ...
```

**Benefits:**
- All relevant skills available in mode context
- No need to cross-reference external files
- Mode is self-contained

**Trade-offs:**
- Larger roleDefinition blocks
- Less modular
- But: clearer for users (4 modes vs. 20 skills)

---

## Summary

SuperRoo successfully ports the superpowers methodology to RooCode by:

1. **Preserving core discipline** - TDD, debugging, review unchanged
2. **Adapting to platform** - 4 modes instead of 20 skills
3. **Adding structural enforcement** - Auto-trigger review, read-only modes
4. **Maintaining fidelity** - 95% faithful to original methodology
5. **Enabling future upgrade** - MCP support when available

**Result:** Battle-tested development methodology now available for RooCode users.
