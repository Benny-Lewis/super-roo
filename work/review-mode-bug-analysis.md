# Review Mode Bug Analysis & Fixes

## Bug Report

**Issue:** When TDD mode spawns code review subtask, it sometimes ends up in wrong mode ("receiving-code-review" instead of "requesting-code-review")

**User Feedback:**
> "it got confused when it spawned a subtask for code review"

## Analysis of Task History

Analyzed `C:\Users\blewis\Downloads\roo_task_nov-25-2025_3-14-03-pm.md` (15,227 lines)

### What Happened

1. **TDD mode correctly requested review** (line 9581-9584):
   ```xml
   <new_task>
   <mode>requesting-code-review</mode>
   <message>Review implementation...</message>
   </new_task>
   ```

2. **First subtask spawn succeeded** (line 9615-9618):
   - Successfully created task in "Requesting Code Review mode" ✅
   - Review completed correctly with feedback
   - Task completed successfully

3. **Second test failed** (from system reminder):
   - Subtask ended up in "receiving-code-review" mode ❌
   - Agent realized wrong mode and tried to switch
   - Confusion about which mode performs reviews

## Root Causes Found

### 1. **Outdated Workspace Rules** (CRITICAL)

`.roo/rules/superroo-workspace.md` was injecting OLD mode names into every conversation:

**Lines 11-14 (OLD):**
```markdown
- **superroo-code** - TDD-driven implementation
- **superroo-debug** - Systematic root-cause debugging
- **superroo-architect** - Design, planning, documentation
- **superroo-review** - Rigorous code review (read-only)
```

**Impact:**
- These old mode names appeared throughout task history (76+ occurrences)
- Agents received conflicting information about which modes exist
- "superroo-review" doesn't exist anymore - it's now "requesting-code-review"
- Created confusion during mode selection

### 2. **Ambiguous Mode Names**

The mode naming was confusing:
- "requesting-code-review" - Sounds like it requests a review (spawns subtask)
- "receiving-code-review" - Sounds like it receives feedback
- But actually: "requesting-code-review" PERFORMS the review

This naming ambiguity contributed to:
- Mode confusion during selection
- Agent reasoning errors about which mode to use

### 3. **Unclear Mode Role Definition**

Original "requesting-code-review" mode definition didn't explicitly state:
- "YOU ARE THE REVIEWER"
- "YOU PERFORM THE REVIEW"
- "DO NOT SPAWN ANOTHER TASK"

## Fixes Applied

### Fix 1: Updated Workspace Rules ✅

**File:** `.roo/rules/superroo-workspace.md`

**Changes:**
- Removed all references to old 4 fat modes
- Added references to new 20 skill-modes
- Updated mode names:
  - superroo-code → test-driven-development
  - superroo-debug → systematic-debugging
  - superroo-architect → brainstorming, writing-plans
  - superroo-review → requesting-code-review
- Added slash command references (/tdd, /debug, etc.)
- Added using-superpowers as entry point

**Lines updated:** 7-28, 62, 79-86

### Fix 2: Clarified Review Mode Role ✅

**File:** `.roomodes` (requesting-code-review mode)

**Changes via `work/fix-review-mode.py`:**
- Added explicit header: "YOU ARE A CODE REVIEWER. YOU PERFORM THE REVIEW. YOU DO NOT SPAWN ANOTHER TASK."
- Clarified "Your Role" section
- Explicitly listed what the mode does and does NOT do
- Added complete review process documentation

## Verification Needed

To verify these fixes work:

1. **Fresh conversation test:**
   - Start new TDD session (workspace rules will load fresh)
   - Implement a feature
   - Verify review subtask spawns in correct mode
   - Verify review performs correctly without trying to spawn another task

2. **Multiple cycles:**
   - TDD → Review → Address Feedback → Re-review
   - Verify mode selection remains correct throughout

3. **Direct review test:**
   - Manually select "requesting-code-review" mode
   - Provide code to review
   - Verify it performs review (doesn't try to spawn another task)

## Expected Behavior After Fixes

✅ TDD mode spawns "requesting-code-review" mode consistently
✅ Review mode performs review without spawning subtasks
✅ Agents don't see conflicting mode names
✅ Workspace rules match actual mode names

## Files Modified

1. `.roo/rules/superroo-workspace.md` - Updated mode references
2. `.roomodes` - requesting-code-review role clarified (via fix-review-mode.py)
3. `work/fix-review-mode.py` - Script that applied fix #2
4. `work/review-mode-bug-analysis.md` - This analysis document

## Next Steps

1. ✅ Fixes applied
2. ⏳ Test TDD → Review flow with fresh conversation
3. ⏳ Verify workspace rules load correctly
4. ⏳ Test multiple composition flows
5. ⏳ Update global installation if tests pass

## Notes

- The inconsistent behavior (worked once, failed once) suggests the workspace rules were causing intermittent confusion
- Fixing workspace rules should prevent agents from seeing old mode names
- Clarifying review mode role prevents confusion if it gets selected incorrectly
- Both fixes work together: prevent wrong selection + handle it gracefully if it happens
