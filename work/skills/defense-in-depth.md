# Defense In Depth

### Skill 6: Defense-in-Depth Validation

      **When:** Invalid data causes failures deep in execution

      **Core Principle:**
      Validate at EVERY layer data passes through. Make bugs structurally impossible.

      **Four Layers:**

      1. **Entry Point Validation** - Reject invalid input at API boundary
         ```typescript
         function createProject(name: string, workingDirectory: string) {
           if (!workingDirectory || workingDirectory.trim() === '') {
             throw new Error('workingDirectory cannot be empty');
           }
           // ...
         }
         ```

      2. **Business Logic Validation** - Ensure data makes sense for operation
         ```typescript
         function initializeWorkspace(projectDir: string) {
           if (!projectDir) {
             throw new Error('projectDir required');
           }
           // ...
         }
         ```

      3. **Environment Guards** - Prevent dangerous operations in specific contexts
         ```typescript
         if (process.env.NODE_ENV === 'test') {
           if (!directory.startsWith(tmpdir())) {
             throw new Error('Refusing operation outside temp dir during tests');
           }
         }
         ```

      4. **Debug Instrumentation** - Capture context for forensics
         ```typescript
         logger.debug('About to perform operation', {
           directory,
           cwd: process.cwd(),
           stack: new Error().stack,
         });
         ```

      **Applying the Pattern:**
      1. Trace the data flow - Where does bad value originate? Where used?
      2. Map all checkpoints - List every point data passes through
      3. Add validation at each layer
      4. Test each layer - Try to bypass layer 1, verify layer 2 catches it

      ---

      ## WORKFLOW SUMMARY

      **As PLAYER (single task):**
      1. Write failing test (RED)
      2. Verify it fails correctly
      3. Write minimal code (GREEN)
      4. Verify it passes
      5. Refactor (stay green)
      6. Auto-trigger code review
      7. Address Critical and Important review feedback
      8. Verify everything passes
      9. NOW task is complete (not before)

      **As CONDUCTOR (multiple tasks):**
      1. Break work into tasks
      2. Spawn new_task for each (subtasks CAN complete and return)
      3. Monitor subtask completion
      4. Auto-trigger review after each subtask
      5. Address feedback from review
      6. Continue to next task
      7. After ALL tasks complete with feedback addressed, main task is complete

      **Always:**
      - Follow TDD (test first, always)
      - Avoid testing anti-patterns
      - Verify before claiming completion
      - Use condition-based waiting for async
      - Apply defense-in-depth for validation
      - Auto-trigger review after implementation
      - Address review feedback before marking complete
      - Task complete = implementation + review + feedback addressed (full cycle)

    whenToUse: |
      Use when implementing features, fixing bugs, or executing implementation plans.
      Enforces TDD discipline with automatic code review after completion.

    groups:
      - read
      - edit
      - command

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- No automatic composition

## Completion Criteria
- (To be defined based on skill content)
