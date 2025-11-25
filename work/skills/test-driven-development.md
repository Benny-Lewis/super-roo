# Test Driven Development

### Skill 1: Test-Driven Development (TDD)

      **When:** Implementing ANY feature or bugfix

      **The Iron Law:**
      ```
      NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
      ```

      **RED-GREEN-REFACTOR Cycle:**

      1. **RED** - Write failing test
         - One behavior
         - Clear name
         - Real code (no mocks unless unavoidable)

      2. **Verify RED** - Watch it fail (MANDATORY)
         ```bash
         npm test path/to/test.test.ts
         ```
         Confirm:
         - Test fails (not errors)
         - Failure message is expected
         - Fails because feature missing (not typos)

      3. **GREEN** - Minimal code to pass
         - Simplest code to pass the test
         - Don't add features, refactor other code, or "improve" beyond the test

      4. **Verify GREEN** - Watch it pass (MANDATORY)
         ```bash
         npm test path/to/test.test.ts
         ```
         Confirm:
         - Test passes
         - Other tests still pass
         - Output pristine (no errors, warnings)

      5. **REFACTOR** - Clean up (stay green)
         - Remove duplication
         - Improve names
         - Extract helpers
         - Keep tests green

      6. **Repeat** - Next failing test for next feature

      **Rationalizations to REJECT:**
      - "Too simple to test"
      - "I'll test after"
      - "Already manually tested"
      - "Deleting X hours is wasteful"
      - "Keep as reference"
      - "TDD will slow me down"
      - "This is different because..."

      **If you wrote code before test:** Delete it. Start over.

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- Spawns: `requesting-code-review`

## Completion Criteria
- (To be defined based on skill content)
