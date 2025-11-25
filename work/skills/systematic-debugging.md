# Systematic Debugging

### Skill 1: Systematic Debugging (4-Phase Framework)

      **When:** Encountering ANY bug, test failure, or unexpected behavior

      **The Iron Law:**
      ```
      NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
      ```

      **The Four Phases (MUST complete each before proceeding):**

      #### Phase 1: Root Cause Investigation

      **BEFORE attempting ANY fix:**

      1. **Read Error Messages Carefully**
         - Don't skip past errors or warnings
         - They often contain the exact solution
         - Read stack traces completely
         - Note line numbers, file paths, error codes

      2. **Reproduce Consistently**
         - Can you trigger it reliably?
         - What are exact steps?
         - Does it happen every time?
         - If not reproducible → gather more data, don't guess

      3. **Check Recent Changes**
         - What changed that could cause this?
         - Git diff, recent commits
         - New dependencies, config changes
         - Environmental differences

      4. **Gather Evidence in Multi-Component Systems**

         **WHEN system has multiple components:**

         **Add diagnostic instrumentation at each boundary:**
         ```
         For EACH component boundary:
           - Log what data enters component
           - Log what data exits component
           - Verify environment/config propagation
           - Check state at each layer

         Run once to gather evidence showing WHERE it breaks
         THEN analyze evidence to identify failing component
         ```

         Example:
         ```bash
         # Layer 1: Workflow
         echo "=== Secrets available: ==="
         echo "VAR: ${VAR:+SET}${VAR:-UNSET}"

         # Layer 2: Build script
         echo "=== Env vars in build: ==="
         env | grep VAR || echo "VAR not in environment"

         # Layer 3: Operation
         echo "=== State: ==="
         # Check actual state
         ```

      5. **Trace Data Flow**

         **WHEN error is deep in call stack:**

         **Use root-cause-tracing (Skill 2) for backward tracing**

         Quick version:
         - Where does bad value originate?
         - What called this with bad value?
         - Keep tracing up until you find the source
         - Fix at source, not at symptom

      #### Phase 2: Pattern Analysis

      1. **Find Working Examples**
         - Locate similar working code in same codebase

      2. **Compare Against References**
         - If implementing pattern, read reference COMPLETELY
         - Don't skim - read every line
         - Understand pattern fully before applying

      3. **Identify Differences**
         - What's different between working and broken?
         - List every difference, however small
         - Don't assume "that can't matter"

      4. **Understand Dependencies**
         - What other components does this need?
         - What settings, config, environment?

      #### Phase 3: Hypothesis and Testing

      1. **Form Single Hypothesis**
         - State clearly: "I think X is root cause because Y"
         - Write it down
         - Be specific

      2. **Test Minimally**
         - SMALLEST possible change to test hypothesis
         - One variable at a time
         - Don't fix multiple things at once

      3. **Verify Before Continuing**
         - Did it work? Yes → Phase 4
         - Didn't work? Form NEW hypothesis
         - DON'T add more fixes on top

      4. **When You Don't Know**
         - Say "I don't understand X"
         - Don't pretend to know
         - Ask for help

      #### Phase 4: Implementation

      1. **Create Failing Test Case**
         - Simplest possible reproduction
         - Automated test if possible
         - MUST have before fixing
         - Use TDD (Skill 3) for writing proper failing tests

      2. **Implement Single Fix**
         - Address root cause identified
         - ONE change at a time
         - No "while I'm here" improvements

      3. **Verify Fix**
         - Test passes now?
         - No other tests broken?
         - Issue actually resolved?

      4. **If Fix Doesn't Work**
         - STOP
         - Count: How many fixes have you tried?
         - If < 3: Return to Phase 1, re-analyze
         - **If ≥ 3: STOP and question the architecture**

      5. **If 3+ Fixes Failed: Question Architecture**
         - Pattern indicating architectural problem:
           - Each fix reveals new problem elsewhere
           - Fixes require massive refactoring
           - Each fix creates new symptoms
         - STOP and question fundamentals
         - Discuss with user before attempting more

      **Red Flags - STOP and Follow Process:**
      - "Quick fix for now, investigate later"
      - "Just try changing X and see"
      - "Add multiple changes, run tests"
      - "Skip test, manually verify"
      - "It's probably X, let me fix that"
      - "I don't fully understand but this might work"
      - "One more fix attempt" (when already tried 2+)
      - Each fix reveals new problem in different place

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- Spawns: `requesting-code-review`

## Completion Criteria
- (To be defined based on skill content)
