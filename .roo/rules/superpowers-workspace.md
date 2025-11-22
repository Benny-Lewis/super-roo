# Superpowers Development Methodology

This workspace enforces superpowers development discipline.

---

## Use Superpowers Modes

For serious work, you MUST use superpowers modes:

- **superpowers-code** - TDD-driven implementation
- **superpowers-debug** - Systematic root-cause debugging
- **superpowers-architect** - Design, planning, documentation
- **superpowers-review** - Rigorous code review (read-only)

**Do NOT bypass superpowers modes for convenience.**

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

Code review is automatic after task completion (superpowers-code/debug).
Catch issues before they compound.

---

## If You're Bypassing Superpowers Modes

**Stop and ask:**
- Why am I not using a superpowers mode?
- Is this serious work? (If yes → use superpowers mode)
- Am I bypassing for convenience? (If yes → stop, use proper mode)

The discipline exists to catch bugs early, maintain quality, and ensure
rigorous development. Bypassing defeats the purpose.

---

**When you start a session, default to superpowers-architect for planning
or superpowers-code for implementation.**
