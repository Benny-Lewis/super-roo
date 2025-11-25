# Testing Skills With Subagents

**Validate skills work under pressure and resist rationalization**

## Overview

Apply RED-GREEN-REFACTOR cycle to process documentation by running baseline tests without the skill, writing skill content to address failures, and iterating until bulletproof against rationalization.

## When to Use

- Creating a new skill (via `writing-skills`)
- Updating an existing skill
- Validating a skill works as intended
- Before deploying skill changes

## The Testing Cycle

### RED: Baseline Without Skill

**1. Create test scenario**
- Realistic task that should trigger skill usage
- Clear success criteria
- Common pitfalls included

**2. Spawn agent WITHOUT the skill**
```
new_task(mode: "test-driven-development", task: "[scenario without skill guidance]")
```

**3. Observe failures**
- What mistakes does agent make?
- Where does it rationalize?
- What steps does it skip?
- What anti-patterns does it fall into?

**4. Document failure modes**
- List specific mistakes observed
- Note rationalization patterns
- Identify missing guidance

### GREEN: Add Skill and Verify

**1. Create/update skill to address failures**
- Add explicit guidance for each failure mode
- Strengthen language where rationalization occurred
- Add red flags for anti-patterns observed

**2. Spawn agent WITH the skill**
```
new_task(mode: "{skill-being-tested}", task: "[same scenario]")
```

**3. Verify improvements**
- Does agent follow the process?
- Are failure modes prevented?
- Does it still rationalize anywhere?

**4. If failures persist: REFACTOR**

### REFACTOR: Close Loopholes

**Iterate until bulletproof:**

**Common loopholes:**
- Vague language → Make explicit
- "Should" or "Consider" → Change to "MUST" or "DO NOT"
- Missing examples → Add concrete examples
- Unclear trigger conditions → Define precisely
- No red flags → Add anti-pattern list

**Example iteration:**
```markdown
❌ BEFORE (agent rationalizes):
"Consider writing tests first"

✅ AFTER (bulletproof):
"NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.
If you wrote code before test: Delete it. Start over."
```

## Real Example: Testing TDD Skill

### RED: Without TDD Skill

**Scenario:** "Implement a prime number checker"

**Agent behavior:**
- Writes implementation first
- Adds tests after
- Rationalizes: "Simple function, tests can come after"

**Failure modes identified:**
1. Writes production code first
2. Rationalizes it's "too simple to test"
3. Doesn't verify RED state

### GREEN: Add TDD Skill

**Skill additions:**
- "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"
- "If you wrote code before test: Delete it. Start over."
- Red flags: "Too simple to test" is rationalization

**Re-test:**
- Agent now writes test first
- Verifies RED
- Implements
- Verifies GREEN

### REFACTOR: Found Edge Case

**Agent still rationalizes:**
- "I'll just sketch the implementation..." (then doesn't delete it)

**Strengthen skill:**
- Add: "Don't 'sketch' implementation. Write test ONLY."
- Add red flag: "'Sketch first' is rationalization"

**Re-test:** Bulletproof

## Test Scenario Library

**Good test scenarios:**
- Feature implementation (tests TDD)
- Bug fix (tests systematic debugging)
- Design question (tests brainstorming)
- Multiple bugs (tests parallel agents)
- Review feedback (tests receiving code review)

**Make scenarios realistic:**
- Include common pitfalls
- Add time pressure elements
- Include rationalizations
- Test edge cases

## Success Criteria

A skill is ready when:
- ✅ Agent follows process without deviation
- ✅ No rationalization occurs
- ✅ All red flags are avoided
- ✅ Process works under pressure
- ✅ Edge cases handled

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- Spawns: Various modes to test (TDD, debug, brainstorm, etc.)
- May spawn: `writing-skills` to iterate on skill content

## Completion Criteria
- Skill tested with realistic scenarios
- All failure modes identified and addressed
- Agent follows skill without rationalization
- Skill is bulletproof
