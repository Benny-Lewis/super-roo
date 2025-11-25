# Verification Before Completion

### Skill 3: Verification Before Completion

      **When:** About to claim work is complete, fixed, or passing

      **The Iron Law:**
      ```
      NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
      ```

      **The Gate Function:**
      ```
      BEFORE claiming any status or expressing satisfaction:

      1. IDENTIFY: What command proves this claim?
      2. RUN: Execute the FULL command (fresh, complete)
      3. READ: Full output, check exit code, count failures
      4. VERIFY: Does output confirm the claim?
         - If NO: State actual status with evidence
         - If YES: State claim WITH evidence
      5. ONLY THEN: Make the claim

      Skip any step = lying, not verifying
      ```

      **Common Failures:**
      | Claim | Requires | Not Sufficient |
      |-------|----------|----------------|
      | Tests pass | Test command output: 0 failures | Previous run, "should pass" |
      | Build succeeds | Build command: exit 0 | Linter passing, logs look good |
      | Bug fixed | Test original symptom: passes | Code changed, assumed fixed |

      **Red Flags - STOP:**
      - Using "should", "probably", "seems to"
      - Expressing satisfaction before verification ("Great!", "Perfect!", "Done!")
      - About to commit/push/PR without verification
      - Relying on partial verification

      **Rationalizations to REJECT:**
      - "Should work now" → RUN the verification
      - "I'm confident" → Confidence ≠ evidence
      - "Just this once" → No exceptions

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- No automatic composition

## Completion Criteria
- (To be defined based on skill content)
