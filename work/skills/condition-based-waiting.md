# Condition Based Waiting

### Skill 5: Condition-Based Waiting

      **When:** Tests have race conditions, timing dependencies, or flaky behavior

      **Core Principle:**
      Wait for the actual condition you care about, not a guess about how long it takes.

      **Pattern:**
      ```typescript
      // ❌ BEFORE: Guessing at timing
      await new Promise(r => setTimeout(r, 50));
      const result = getResult();

      // ✅ AFTER: Waiting for condition
      await waitFor(() => getResult() !== undefined);
      const result = getResult();
      ```

      **Implementation:**
      ```typescript
      async function waitFor<T>(
        condition: () => T | undefined | null | false,
        description: string,
        timeoutMs = 5000
      ): Promise<T> {
        const startTime = Date.now();
        while (true) {
          const result = condition();
          if (result) return result;
          if (Date.now() - startTime > timeoutMs) {
            throw new Error(`Timeout waiting for ${description} after ${timeoutMs}ms`);
          }
          await new Promise(r => setTimeout(r, 10)); // Poll every 10ms
        }
      }
      ```

      **When Arbitrary Timeout IS Correct:**
      - Testing actual timing behavior (debounce, throttle)
      - Based on known timing (not guessing)
      - Must document WHY with comment

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- No automatic composition

## Completion Criteria
- (To be defined based on skill content)
