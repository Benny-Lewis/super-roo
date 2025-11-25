# Testing Anti Patterns

### Skill 2: Testing Anti-Patterns

      **When:** Writing or changing tests, adding mocks

      **The Iron Laws:**
      ```
      1. NEVER test mock behavior
      2. NEVER add test-only methods to production classes
      3. NEVER mock without understanding dependencies
      ```

      **Anti-Pattern 1: Testing Mock Behavior**
      ```typescript
      // ❌ BAD: Testing that the mock exists
      expect(screen.getByTestId('sidebar-mock')).toBeInTheDocument();

      // ✅ GOOD: Test real component
      expect(screen.getByRole('navigation')).toBeInTheDocument();
      ```

      **Gate Function:**
      ```
      BEFORE asserting on any mock element:
        Ask: "Am I testing real component behavior or just mock existence?"
        IF testing mock existence: STOP - unmock the component
      ```

      **Anti-Pattern 2: Test-Only Methods in Production**
      ```typescript
      // ❌ BAD: destroy() only used in tests
      class Session {
        async destroy() { ... }
      }

      // ✅ GOOD: Test utilities handle test cleanup
      export async function cleanupSession(session: Session) { ... }
      ```

      **Gate Function:**
      ```
      BEFORE adding any method to production class:
        Ask: "Is this only used by tests?"
        IF yes: STOP - Put it in test utilities instead
      ```

      **Anti-Pattern 3: Mocking Without Understanding**
      ```
      BEFORE mocking any method:
        STOP - Don't mock yet
        1. Ask: "What side effects does the real method have?"
        2. Ask: "Does this test depend on any of those side effects?"
        3. Run test with real implementation FIRST
        4. THEN add minimal mocking at the right level
      ```

      **Anti-Pattern 4: Incomplete Mocks**
      ```
      BEFORE creating mock responses:
        Check: "What fields does the real API response contain?"
        Include ALL fields system might consume downstream
        Partial mocks fail silently
      ```

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- No automatic composition

## Completion Criteria
- (To be defined based on skill content)
