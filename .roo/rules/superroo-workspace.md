# SuperRoo Development Methodology

This workspace enforces SuperRoo development discipline.

---

## Use SuperRoo Modes

For serious work, you MUST use SuperRoo modes:

- **superroo-code** - TDD-driven implementation
- **superroo-debug** - Systematic root-cause debugging
- **superroo-architect** - Design, planning, documentation
- **superroo-review** - Rigorous code review (read-only)

**Do NOT bypass SuperRoo modes for convenience.**

Only use other modes for:
- ⚠️ Trivial one-off tasks explicitly marked as experimental
- ⚠️ User explicitly requests different mode
- ⚠️ Quick questions that don't involve code changes

When in doubt, use a superpowers mode. They exist for a reason.

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

Code review is automatic after task completion (superroo-code/debug).
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

**When you start a session, default to superroo-architect for planning
or superroo-code for implementation.**
