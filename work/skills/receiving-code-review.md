# Receiving Code Review

**How to process and respond to code review feedback**

## Overview

This skill guides you through receiving and addressing code review feedback with technical rigor, not performative agreement.

## Core Principles

### Technical Rigor Over Agreement

- **Question feedback** - Don't blindly implement suggestions
- **Verify assumptions** - Check if feedback applies to your context
- **Push back respectfully** - If feedback seems incorrect, investigate and discuss
- **Never performatively agree** - Don't say "good point" unless you genuinely agree

### Evidence-Based Responses

Before implementing review feedback:
1. **Understand the issue** - What problem is the feedback addressing?
2. **Verify it's actually a problem** - Does it apply in this context?
3. **Consider alternatives** - Is the suggested fix the best approach?
4. **Test the change** - Use TDD if fixing issues

## Workflow

### 1. Read All Feedback First

- Don't respond to items one-by-one
- Get full context of all issues
- Look for patterns or themes

### 2. Categorize Feedback

**Critical Issues (must address):**
- Security vulnerabilities
- Logic bugs
- Requirements not met
- Missing tests

**Suggestions (evaluate carefully):**
- Code quality improvements
- Better patterns
- Performance optimizations

**Questions (discuss/clarify):**
- Unclear design decisions
- Context the reviewer may be missing

### 3. Respond to Each Item

For each piece of feedback:

**If you agree:**
- Acknowledge the issue
- Fix using TDD (write test, watch fail, fix, verify pass)
- Mark as resolved with evidence

**If unclear:**
- Ask clarifying questions
- Provide context the reviewer may be missing
- Discuss alternative approaches

**If you disagree:**
- Explain why respectfully
- Provide technical reasoning
- Offer evidence or counter-examples
- Be open to being wrong

### 4. Make Changes Using TDD

When fixing issues from review:
- Write test that fails due to the issue
- Fix the issue
- Verify test passes
- Refactor if needed

### 5. Request Re-Review

After addressing feedback:
- Summarize what was changed
- Call out anything not addressed and why
- Request new_task with requesting-code-review

## Red Flags (Don't Do This)

❌ "Great catch!" without understanding
❌ Implementing suggestions blindly
❌ Defensive responses without investigation
❌ Ignoring feedback without discussion
❌ Batch-fixing without testing each change

## Example Response Pattern

**Reviewer:** "This function has O(n²) complexity, use a Set instead"

**Good Response:**
"Let me verify the complexity issue first..."
[Investigates with profiling]
"You're right, profiling shows it's slow with 1000+ items. Adding test for performance requirement, then switching to Set."
[Implements fix with TDD]
"Fixed in commit abc123. Test now verifies <100ms for 10k items."

**Bad Response:**
"Good point! Will fix."
[Changes without testing or understanding]

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- After addressing feedback: spawn `verification-before-completion` to verify fixes
- May spawn `test-driven-development` for each fix

## Completion Criteria
- All feedback addressed or discussed
- Changes made using TDD
- Tests pass
- Re-review requested if needed
