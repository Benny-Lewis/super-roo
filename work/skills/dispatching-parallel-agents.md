# Dispatching Parallel Agents

**Spawn multiple independent investigations concurrently**

## When to Use

Use this skill when facing 3+ independent problems that can be investigated without shared state or dependencies.

**Examples:**
- Multiple failing tests with different root causes
- Several bugs across unrelated features
- Independent feature implementations
- Multiple code review items that don't interact

**Don't use when:**
- Problems might have shared root cause
- Changes might conflict
- Dependencies between tasks
- Fewer than 3 independent items

## Workflow

### 1. Analyze Independence

For each problem:
- Can it be investigated without knowledge of others?
- Do changes conflict with other problems?
- Are there shared dependencies?

If yes to any: Problems are NOT independent, don't use parallel agents.

### 2. Create Clear Task Descriptions

For each independent problem:
- Write clear, standalone description
- Include all context needed
- Specify success criteria
- No cross-references to other tasks

### 3. Spawn Agents Concurrently

Use new_task for each:
```
new_task(mode: "systematic-debugging", task: "Fix bug 1: [description]")
new_task(mode: "systematic-debugging", task: "Fix bug 2: [description]")
new_task(mode: "systematic-debugging", task: "Fix bug 3: [description]")
```

Or for features:
```
new_task(mode: "test-driven-development", task: "Implement feature A: [description]")
new_task(mode: "test-driven-development", task: "Implement feature B: [description]")
```

### 4. Monitor Completion

- Wait for all agents to complete
- Each returns summary independently
- No agent depends on another's results

### 5. Integrate Results

After all complete:
- Review all summaries
- Check for unexpected interactions
- Verify all tests pass together
- Spawn `requesting-code-review` for integrated changes

## Example: Multiple Bugs

**Scenario:** 3 failing tests, different features

```
Bug 1: Login fails with empty email
Bug 2: Logout button doesn't appear
Bug 3: Profile page shows wrong username
```

**Analysis:** These are independent
- Different features (auth, UI, profile)
- No shared code paths
- Can fix in any order

**Dispatch:**
```
new_task(mode: "systematic-debugging", task: "Fix: Login fails with empty email. Investigate validation logic, create failing test, fix root cause.")

new_task(mode: "systematic-debugging", task: "Fix: Logout button doesn't appear. Investigate UI rendering, create failing test, fix root cause.")

new_task(mode: "systematic-debugging", task: "Fix: Profile page shows wrong username. Investigate profile data loading, create failing test, fix root cause.")
```

**Integration:**
- All 3 agents complete independently
- Review summaries
- Verify all 3 fixes work together
- Request code review for all changes

## Red Flags (Don't Do This)

❌ Spawning agents for dependent problems
❌ Starting parallel work before analyzing independence
❌ Creating vague task descriptions
❌ Skipping integration testing
❌ Not reviewing all summaries before proceeding

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- Spawns: Multiple `systematic-debugging` or `test-driven-development` agents
- After all complete: spawn `requesting-code-review`

## Completion Criteria
- All spawned agents completed
- Summaries reviewed
- Integration verified
- Tests pass
