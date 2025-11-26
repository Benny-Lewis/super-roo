---
description: Execute plan in batches with review checkpoints
---

Switch to executing-plans mode and execute the implementation plan:

**Process:**
1. Load and review plan critically
2. Create TodoWrite with all tasks
3. Execute in batches (default: 3 tasks at a time)
4. Report after each batch: "Ready for feedback."
5. Apply feedback and continue

**When to STOP:**
- Hit blocker mid-batch
- Plan has critical gaps
- Don't understand instruction
- Verification fails repeatedly

Ask for clarification rather than guessing.

After all tasks complete, use finishing-a-development-branch workflow.
