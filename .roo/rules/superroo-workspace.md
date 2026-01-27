# SuperRoo Development Methodology

This workspace enforces SuperRoo development discipline.

---

## Use SuperRoo Skill-Modes

For serious work, you MUST use SuperRoo skill-modes. Start with:
- **using-superpowers** - Entry point that selects the right skill

Or use slash commands for quick access:
- `/tdd` - Test-driven development
- `/debug` - Systematic debugging
- `/brainstorm` - Design refinement
- `/write-plan` - Create implementation plan
- `/execute-plan` - Execute plan with TDD
- `/review` - Request code review

Or select directly from 21 skill-modes:
- **test-driven-development** - RED-GREEN-REFACTOR cycle
- **systematic-debugging** - 4-phase root-cause investigation
- **brainstorming** - Socratic design refinement
- **writing-plans** - Comprehensive implementation plans
- **executing-plans** - Batch execution with review checkpoints
- **requesting-code-review** - Perform rigorous code review
- **receiving-code-review** - Process review feedback
- And 14 more specialized skills...

**Do NOT bypass SuperRoo modes for convenience.**

Only use other modes for:
- ⚠️ Trivial one-off tasks explicitly marked as experimental
- ⚠️ User explicitly requests different mode
- ⚠️ Quick questions that don't involve code changes

When in doubt, use a skill-mode. They exist for a reason.

---

## Core Principles (Non-Negotiable)

These apply ALWAYS, even if temporarily outside superpowers modes:

### 🔴 NO CODE WITHOUT FAILING TEST FIRST

Write the test, watch it fail, then implement.
If you didn't watch it fail, it proves nothing.

### ✅ NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION

Before saying "done," "fixed," or "passing," run the verification command
and show the output. Evidence before assertions, always.

### 🔍 ROOT CAUSE INVESTIGATION BEFORE FIXES

No fixes without understanding the root cause first.
Patching symptoms creates more bugs.

### 👁️ REVIEW EARLY, REVIEW OFTEN

Code review is automatic after task completion (test-driven-development/systematic-debugging).
Catch issues before they compound.

---

## If You're Bypassing SuperRoo Modes

**Stop and ask:**
- Why am I not using a SuperRoo mode?
- Is this serious work? (If yes → use SuperRoo mode)
- Am I bypassing for convenience? (If yes → stop, use proper mode)

The discipline exists to catch bugs early, maintain quality, and ensure
rigorous development. Bypassing defeats the purpose.

---

**When you start a session, select the appropriate SuperRoo skill-mode:**
- using-superpowers for automatic skill selection
- brainstorming for design refinement
- writing-plans for implementation planning
- test-driven-development for feature implementation
- systematic-debugging for investigating bugs
- requesting-code-review for code review only
- Or use slash commands: /tdd, /debug, /brainstorm, /write-plan, /execute-plan
