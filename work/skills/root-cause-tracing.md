# Root Cause Tracing

### Skill 2: Root Cause Tracing

      **When:** Errors occur deep in execution, need to trace back to original trigger

      **Core Principle:**
      Trace backward through call chain until you find original trigger, then fix at source.

      **The Tracing Process:**

      1. **Observe the Symptom**
         ```
         Error: git init failed in /project/source
         ```

      2. **Find Immediate Cause**
         What code directly causes this?
         ```typescript
         await execFileAsync('git', ['init'], { cwd: projectDir });
         ```

      3. **Ask: What Called This?**
         ```typescript
         WorktreeManager.createWorktree(projectDir)
           → called by Session.initialize()
           → called by Session.create()
           → called by test
         ```

      4. **Keep Tracing Up**
         What value was passed?
         - `projectDir = ''` (empty string!)
         - Empty string resolves to `process.cwd()`

      5. **Find Original Trigger**
         Where did empty string come from?
         ```typescript
         const context = setupTest(); // Returns { tempDir: '' }
         create('name', context.tempDir); // Accessed before initialization!
         ```

      **Adding Stack Traces:**

      When you can't trace manually, add instrumentation:

      ```typescript
      async function operation(directory: string) {
        const stack = new Error().stack;
        console.error('DEBUG operation:', {
          directory,
          cwd: process.cwd(),
          nodeEnv: process.env.NODE_ENV,
          stack,
        });

        await doOperation(directory);
      }
      ```

      **Critical:** Use `console.error()` in tests (not logger)

      **Run and capture:**
      ```bash
      npm test 2>&1 | grep 'DEBUG operation'
      ```

      **Analyze stack traces:**
      - Look for test file names
      - Find line number triggering call
      - Identify pattern

      **NEVER fix just where error appears. Trace back to original trigger.**

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- No automatic composition

## Completion Criteria
- (To be defined based on skill content)
