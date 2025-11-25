# Writing Plans

### Skill 2: Writing Plans

      **When:** Design complete, need detailed implementation tasks

      **Overview:**
      Write comprehensive plans assuming engineer has zero context.
      Exact file paths, complete code, verification steps. Bite-sized tasks.

      **Plan Document Header (MUST include):**
      ```markdown
      # [Feature Name] Implementation Plan

      **Goal:** [One sentence]

      **Architecture:** [2-3 sentences]

      **Tech Stack:** [Key technologies]

      ---
      ```

      **Bite-Sized Task Granularity (each step 2-5 minutes):**
      - "Write the failing test" - step
      - "Run it to make sure it fails" - step
      - "Implement minimal code to pass" - step
      - "Run tests and verify pass" - step
      - "Commit" - step

      **Task Structure:**
      ```markdown
      ### Task N: [Component Name]

      **Files:**
      - Create: `exact/path/to/file.py`
      - Modify: `exact/path/existing.py:123-145`
      - Test: `tests/exact/path/test.py`

      **Step 1: Write the failing test**
      [Complete code]

      **Step 2: Run test to verify it fails**
      Run: [exact command]
      Expected: [exact output]

      **Step 3: Write minimal implementation**
      [Complete code]

      **Step 4: Run test to verify it passes**
      Run: [exact command]
      Expected: [exact output]

      **Step 5: Commit**
      [exact git commands]
      ```

      **Remember:**
      - Exact file paths always
      - Complete code in plan
      - Exact commands with expected output
      - DRY, YAGNI, TDD, frequent commits

      **Save to:** `docs/plans/YYYY-MM-DD-<feature>.md`

      **Execution Handoff:**
      After saving plan, offer:
      1. Subagent-Driven (this session) - Use Skill 6
      2. Parallel Session (separate) - Use Skill 3

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- Spawns: `executing-plans`

## Completion Criteria
- (To be defined based on skill content)
