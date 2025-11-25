# Executing Plans

### Skill 3: Executing Plans

      **When:** Partner provides complete plan to execute in batches

      **The Process:**

      **Step 1: Load and Review Plan**
      - Read plan file
      - Review critically
      - If concerns: Raise with user
      - If no concerns: Create TodoWrite, proceed

      **Step 2: Execute Batch (default: first 3 tasks)**
      For each task:
      - Mark as in_progress
      - Follow steps exactly
      - Run verifications
      - Mark as completed

      **Step 3: Report**
      - Show what implemented
      - Show verification output
      - Say: "Ready for feedback."

      **Step 4: Continue**
      - Apply changes if needed
      - Execute next batch
      - Repeat

      **Step 5: Complete Development**
      After all tasks complete:
      - Use finishing-a-development-branch skill (Skill 5)

      **When to STOP:**
      - Hit blocker mid-batch
      - Plan has critical gaps
      - Don't understand instruction
      - Verification fails repeatedly

      **Ask for clarification rather than guessing.**

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- Spawns: `test-driven-development`

## Completion Criteria
- (To be defined based on skill content)
