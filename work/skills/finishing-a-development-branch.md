# Finishing A Development Branch

### Skill 5: Finishing a Development Branch

      **When:** Implementation complete, all tests pass

      **The Process:**

      **Step 1: Verify Tests**
      Run test suite. If fails: STOP, cannot proceed.

      **Step 2: Determine Base Branch**
      Identify base (usually main/master).

      **Step 3: Present Options**
      ```
      Implementation complete. What would you like to do?

      1. Merge back to <base> locally
      2. Push and create a Pull Request
      3. Keep the branch as-is
      4. Discard this work

      Which option?
      ```

      **Step 4: Execute Choice**

      - **Option 1:** Merge locally, verify tests, cleanup
      - **Option 2:** Push, create PR, cleanup
      - **Option 3:** Keep as-is (don't cleanup)
      - **Option 4:** Confirm, then discard and cleanup

      **Step 5: Cleanup Worktree**
      For Options 1, 2, 4: Remove worktree
      For Option 3: Keep worktree

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- No automatic composition

## Completion Criteria
- (To be defined based on skill content)
