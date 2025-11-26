---
description: Complete development work (verify, merge, PR, or cleanup)
---

Switch to finishing-a-development-branch mode and finish the development branch:

**Process:**

**Step 1: Verify Tests**
Run test suite. If tests fail: STOP, cannot proceed.

**Step 2: Present Options**
```
Implementation complete. What would you like to do?

1. Merge back to main locally
2. Push and create a Pull Request
3. Keep the branch as-is
4. Discard this work

Which option?
```

**Step 3: Execute Choice**
- Option 1: Merge locally, verify tests on merged result, cleanup worktree
- Option 2: Push branch, create PR, cleanup worktree
- Option 3: Keep as-is (preserve worktree)
- Option 4: Confirm "discard", then delete and cleanup

**Never:**
- Proceed with failing tests
- Merge without verifying tests on result
- Delete work without confirmation
