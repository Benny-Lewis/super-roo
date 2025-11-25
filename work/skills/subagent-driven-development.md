# Subagent Driven Development

### Skill 6: Subagent-Driven Development

      **When:** Executing plans with independent tasks in current session

      **The Process:**

      **1. Load Plan**
      Read plan, create TodoWrite with all tasks.

      **2. Execute Task with Subagent**
      Dispatch fresh subagent:
      ```
      Task tool:
        "Implement Task N: [name]"
        Read task, implement exactly, write tests, verify, commit, report
      ```

      **3. Review Subagent's Work**
      Dispatch code-reviewer subagent using superroo-review mode

      **4. Apply Review Feedback**
      - Fix Critical issues immediately
      - Fix Important issues before next
      - Note Minor issues

      **5. Mark Complete, Next Task**
      Repeat steps 2-5 for all tasks

      **6. Final Review**
      Dispatch final code-reviewer for entire implementation

      **7. Complete Development**
      Use finishing-a-development-branch skill (Skill 5)

      **Advantages:**
      - Fresh context per task
      - Review checkpoints automatic
      - Catches issues early

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- Spawns: `test-driven-development`

## Completion Criteria
- (To be defined based on skill content)
