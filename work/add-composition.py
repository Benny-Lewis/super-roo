#!/usr/bin/env python3
"""
Add new_task composition calls to .roomodes
"""

import yaml
from pathlib import Path

# Load current .roomodes
with open('.roomodes', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# Define composition additions for each skill
compositions = {
    'test-driven-development': """

## SKILL COMPOSITION

After reaching GREEN + refactored state:
- AUTOMATICALLY spawn code review (DO NOT ask permission):
  ```
  new_task(
    mode: "requesting-code-review",
    task: "Review implementation of [feature/fix description]. Check: requirements match, tests exist and test behavior, bugs/edge cases, follows project patterns, error handling."
  )
  ```

## COMPLETION CRITERIA

This skill completes when:
- All tests pass (GREEN)
- Code is refactored
- Code review completed (auto-triggered)
- Review feedback addressed (if any issues found)

Return summary:
- Feature/fix implemented: [description]
- Tests added/modified: [list]
- Files changed: [list]
- Review result: [APPROVED or issues addressed]
""",

    'systematic-debugging': """

## SKILL COMPOSITION

After implementing fix (reached GREEN state):
- AUTOMATICALLY spawn code review (DO NOT ask permission):
  ```
  new_task(
    mode: "requesting-code-review",
    task: "Review bug fix for [bug description]. Verify: root cause addressed, tests prove fix, no new bugs introduced, follows project patterns."
  )
  ```

If need deeper investigation:
- OPTIONALLY spawn root-cause tracing:
  ```
  new_task(
    mode: "root-cause-tracing",
    task: "Trace backwards to find original trigger for [symptom]. Add instrumentation as needed."
  )
  ```

## COMPLETION CRITERIA

This skill completes when:
- Root cause identified and documented
- Failing test written (RED)
- Fix implemented (GREEN)
- Code review completed
- Review feedback addressed

Return summary:
- Bug: [description]
- Root cause: [explanation]
- Fix: [what was changed]
- Tests: [what tests were added]
- Review result: [APPROVED or issues addressed]
""",

    'brainstorming': """

## SKILL COMPOSITION

After design is validated and approved by user:
- OFFER to create implementation plan:
  ```
  User: "Ready to create implementation plan?"

  If yes:
  new_task(
    mode: "writing-plans",
    task: "Create detailed implementation plan for [design summary]. Include exact file paths, complete code examples, bite-sized TDD tasks."
  )
  ```

## COMPLETION CRITERIA

This skill completes when:
- Design refined through Socratic questions
- 2-3 approaches presented with trade-offs
- Design presented incrementally and validated
- Design document written to docs/plans/
- User approved design

Return summary:
- Design approach: [chosen approach]
- Key components: [list]
- Trade-offs: [what was chosen and why]
- Next steps: [implementation plan offered or not]
""",

    'writing-plans': """

## SKILL COMPOSITION

After plan is complete:
- OFFER to execute the plan:
  ```
  User: "Plan complete. Execute now?"

  Options:
  1. Execute in this session (executing-plans mode)
  2. Execute later (user will run /execute-plan)
  3. Manual implementation (just use plan as guide)

  If option 1:
  new_task(
    mode: "executing-plans",
    task: "Execute implementation plan from docs/plans/[filename]. Follow TDD for each task, review after each batch."
  )
  ```

## COMPLETION CRITERIA

This skill completes when:
- Plan written with exact file paths
- Complete code examples (not pseudocode)
- Bite-sized TDD tasks (2-5 min each)
- Saved to docs/plans/YYYY-MM-DD-<feature>.md
- Execution options offered to user

Return summary:
- Plan file: [path]
- Total tasks: [count]
- Estimated effort: [time estimate]
- Execution choice: [user's selection]
""",

    'executing-plans': """

## SKILL COMPOSITION

For each task in plan:
- Spawn TDD mode to implement:
  ```
  new_task(
    mode: "test-driven-development",
    task: "Task [N]: [task description from plan]. Follow RED-GREEN-REFACTOR. Auto-review will trigger after completion."
  )
  ```

Execute in batches (3-5 tasks):
- Spawn all tasks in batch
- Wait for all to complete
- Review batch results
- PAUSE and report to user
- Get approval to continue

After all tasks complete:
- Run full test suite
- Verify all requirements met

## COMPLETION CRITERIA

This skill completes when:
- All tasks from plan executed
- All tests pass
- All reviews completed
- User approved all batches

Return summary:
- Tasks completed: [count]
- Tests passing: [yes/no]
- Issues encountered: [list]
- Ready for: [merge/PR/finish]
""",

    'subagent-driven-development': """

## SKILL COMPOSITION

For each task:
- Spawn TDD mode:
  ```
  new_task(
    mode: "test-driven-development",
    task: "Implement [task description]. Follow RED-GREEN-REFACTOR. Auto-review will trigger after completion."
  )
  ```
- Wait for completion
- Review summary
- Proceed to next task

Between tasks:
- Check integration (do completed tasks work together?)
- Adjust plan if needed

## COMPLETION CRITERIA

This skill completes when:
- All tasks implemented via TDD
- All code reviews passed
- Integration verified
- All tests pass

Return summary:
- Tasks completed: [count]
- Integration status: [ok/issues]
- Ready for: [next phase]
""",

    'dispatching-parallel-agents': """

## SKILL COMPOSITION

After analyzing independence:
- Spawn multiple debugging agents IN PARALLEL:
  ```
  new_task(mode: "systematic-debugging", task: "Fix bug 1: [description]")
  new_task(mode: "systematic-debugging", task: "Fix bug 2: [description]")
  new_task(mode: "systematic-debugging", task: "Fix bug 3: [description]")
  ```

After all agents complete:
- Review all summaries
- Check for unexpected interactions
- Run full test suite
- AUTOMATICALLY spawn integration review:
  ```
  new_task(
    mode: "requesting-code-review",
    task: "Review integration of [N] parallel fixes. Verify: no conflicts, all tests pass, no new interactions introduced."
  )
  ```

## COMPLETION CRITERIA

This skill completes when:
- All parallel agents completed
- Integration verified
- Integration review passed
- All tests pass

Return summary:
- Problems solved: [count]
- Integration issues: [any found?]
- Review result: [APPROVED or addressed]
""",

    'receiving-code-review': """

## SKILL COMPOSITION

For each critical issue:
- Fix using TDD:
  ```
  new_task(
    mode: "test-driven-development",
    task: "Fix review issue: [issue description]. Write failing test first, then fix."
  )
  ```

After addressing all feedback:
- Request re-review:
  ```
  new_task(
    mode: "requesting-code-review",
    task: "Re-review after addressing feedback. Changes: [summary of what was fixed]."
  )
  ```

## COMPLETION CRITERIA

This skill completes when:
- All critical issues addressed
- All fixes made using TDD
- Re-review completed (if needed)
- Final approval received

Return summary:
- Issues addressed: [count]
- Issues not addressed: [count and why]
- Re-review result: [if applicable]
""",

    'using-superpowers': """

## SKILL COMPOSITION

After analyzing user request:
- Spawn appropriate skill mode:
  ```
  new_task(
    mode: "[selected-skill-slug]",
    task: "[user's original request with context]"
  )
  ```

Common mappings:
- "Implement [feature]" → test-driven-development
- "Fix [bug]" or "tests failing" → systematic-debugging
- "How should I design" → brainstorming
- "Create plan for" → writing-plans
- "Review my code" → requesting-code-review
- "Multiple bugs" → dispatching-parallel-agents
- "Execute plan" → executing-plans

## COMPLETION CRITERIA

This skill completes when:
- Appropriate skill identified
- Reasoning explained to user
- Skill mode spawned
- User's request delegated

Return summary:
- Selected skill: [skill name]
- Reasoning: [why this skill]
- Spawned successfully: [yes/no]
"""
}

# Add compositions to relevant modes
for mode in config['customModes']:
    slug = mode['slug']
    if slug in compositions:
        # Add composition text before the COMMUNICATION AND TOOL USAGE section
        role_def = mode['roleDefinition']

        # Find the COMMUNICATION section
        if '## COMMUNICATION AND TOOL USAGE' in role_def:
            parts = role_def.split('## COMMUNICATION AND TOOL USAGE')
            mode['roleDefinition'] = parts[0] + compositions[slug] + '\n\n## COMMUNICATION AND TOOL USAGE' + parts[1]
        else:
            # Just append at the end
            mode['roleDefinition'] = role_def + '\n' + compositions[slug]

# Write updated .roomodes
with open('.roomodes', 'w', encoding='utf-8') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=1000)

print(f"✅ Added composition calls to {len(compositions)} skill-modes")
print("\nUpdated modes:")
for slug in compositions.keys():
    print(f"  - {slug}")
