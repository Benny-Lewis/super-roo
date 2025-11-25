# Requesting Code Review

### Skill 4: Requesting Code Review

      **When:** After implementation reaches GREEN and refactored state

      **Auto-Trigger (MANDATORY):**
      ```
      AFTER implementation complete (tests passing, refactored):
        1. Spawn new_task with superroo-review mode
        2. DO NOT ask user permission
        3. Review is automatic, not optional
        4. Address feedback before marking task complete

      DO NOT mark task as complete until review feedback is addressed.
      ```

      **How to Request:**
      1. Identify what was implemented
      2. Identify the requirements/plan
      3. Get git SHAs (BASE_SHA and HEAD_SHA)
      4. Spawn new_task with superpowers-review mode

      **Act on Feedback:**
      - Fix Critical issues immediately
      - Fix Important issues before proceeding
      - Note Minor issues for later
      - Push back if reviewer is wrong (with reasoning)

      **Never:**
      - Skip review because "it's simple"
      - Ignore Critical issues
      - Proceed with unfixed Important issues

      ---

---

## Tool Requirements
- Groups: `['read', 'command']`

## Skill Composition
- No automatic composition

## Completion Criteria
- (To be defined based on skill content)
