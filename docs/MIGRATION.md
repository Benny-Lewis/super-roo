# Migration Guide: 4 Modes → 21 Skill-Modes

**From:** superroo v1 (4 fat modes)
**To:** superroo v2 (21 skill-modes)

---

## Why We Redesigned

**Goal:** Achieve 90% fidelity to [obra/superpowers](https://github.com/obra/superpowers)

**Changes:**
- 4 fat modes → 21 skill-modes (adapted from obra skills)
- Embedded skills → One mode per skill
- Shared context → Isolated subtasks via `new_task`
- Mode-centric → Skill-centric mental model

---

## Quick Comparison

| Old (v1) | New (v2) |
|----------|----------|
| superroo-code | test-driven-development |
| superroo-debug | systematic-debugging |
| superroo-architect | brainstorming, writing-plans, executing-plans |
| superroo-review | requesting-code-review |
| (no entry point) | using-superpowers |

---

## What Changed

### 1. Mode Selection

**Old:** Pick from 4 modes
```
- superroo-code (TDD + 5 other skills)
- superroo-debug (debugging + 7 other skills)
- superroo-architect (planning + 7 other skills)
- superroo-review (review only)
```

**New:** Pick from 21 skill-modes OR use entry point
```
- using-superpowers (entry point, recommends skill)
- Or direct: test-driven-development, systematic-debugging, etc.
- Or slash commands: /tdd, /debug, /brainstorm
```

### 2. Skill Composition

**Old:** Embedded skills in fat modes
```
superroo-code mode has:
- TDD skill (embedded)
- Testing anti-patterns (embedded)
- Verification (embedded)
- ... (all in one mode)
```

**New:** Skills invoke other skills explicitly
```
test-driven-development mode:
- Implements using TDD
- AUTOMATICALLY spawns requesting-code-review
- Review returns feedback
- TDD mode addresses feedback
```

### 3. Context Isolation

**Old:** Hierarchical subtasks (shared context)
**New:** Isolated subtasks (separate conversation history)

---

## Migration Steps

### If Using Global Installation

**Step 1:** Backup old version (optional)
```bash
# In super-roo directory
cp .roomodes .roomodes.v1.backup
```

**Step 2:** Pull latest changes
```bash
git pull origin main
# Or checkout the skill-modes-redesign branch
```

**Step 3:** Update RooCode settings
```bash
# Windows
copy .roomodes %APPDATA%\Code\User\roo-code-settings\customModes.json

# macOS/Linux
cp .roomodes ~/.config/Code/User/roo-code-settings/customModes.json
```

**Step 4:** Restart VS Code

**Step 5:** Verify
- Open mode selector
- Should see 21 skill-modes
- Test: `/tdd`, `/debug`, `/brainstorm` commands

### If Using Project-Specific Installation

**Step 1:** Backup old `.roomodes` in your project
```bash
cd your-project
cp .roomodes .roomodes.v1.backup
```

**Step 2:** Copy new version
```bash
cp /path/to/super-roo/.roomodes .
cp -r /path/to/super-roo/.roo .
```

**Step 3:** Verify with RooCode

---

## Updated Workflows

### Old: Feature Implementation
```
1. Select superroo-architect
2. Brainstorm design
3. Write plan
4. Switch to superroo-code
5. Implement tasks
6. Switch to superroo-architect
7. Finish branch
```

### New: Feature Implementation
```
1. Select using-superpowers (or /brainstorm)
2. brainstorming mode → refines design
3. Offers writing-plans
4. writing-plans mode → creates plan
5. Offers executing-plans
6. executing-plans → spawns test-driven-development per task
7. Each task auto-reviews
8. Use finishing-a-development-branch when done
```

**Or use direct mode selection:**
```
/brainstorm → refine design
/write-plan → create plan
/execute-plan → implement with TDD
```

---

## Troubleshooting

### "I don't see 21 modes in dropdown"

**Check:**
1. Did you restart VS Code?
2. Is `.roomodes` in the right location?
   - Global: `~/.config/Code/User/roo-code-settings/customModes.json`
   - Project: `.roomodes` in project root
3. Is YAML valid? Test with: `python3 -c "import yaml; yaml.safe_load(open('.roomodes'))"`

### "Slash commands don't work"

**Check:**
1. Are command files in `.roo/commands/`?
2. Did you copy the `.roo/` directory?
3. Restart VS Code

### "Skills don't auto-compose"

**This is expected behavior** - Skills use `new_task()` which RooCode handles. If subtasks aren't spawning:
1. Check RooCode version (may need latest)
2. Look for `new_task` calls in mode definitions
3. Check if auto-approval is blocking (configure auto-approval for subtasks)

### "I prefer the old 4-mode system"

You can revert:
```bash
# Restore v1 backup
cp .roomodes.v1.backup .roomodes

# Or checkout old version
git checkout <commit-before-redesign>
```

---

## What Stayed The Same

✅ **Core principles** - TDD, verification, root-cause debugging unchanged
✅ **Auto-review** - Still automatic after task completion
✅ **All workflows** - Every workflow from v1 still works
✅ **Slash commands** - `/brainstorm`, `/write-plan`, `/execute-plan` still work
✅ **Installation** - Same installation process

---

## Benefits of v2

### For Users
- **Clearer mental model** - "I'm using the TDD skill" vs "I'm in code mode"
- **Lighter context** - Only active skill loaded (not 6-8 skills)
- **Better isolation** - Subtask details don't pollute parent conversation
- **Easier to learn** - One skill at a time vs understanding 4 complex modes

### For Compatibility
- **90% fidelity** to obra/superpowers (up from 75%)
- **1:1 skill mapping** - Each obra skill = one SuperRoo mode
- **Skill composability** - Skills invoke skills (just like obra)
- **Isolated contexts** - True independent execution

---

## Getting Help

**Issues:** [GitHub Issues](https://github.com/Benny-Lewis/super-roo/issues)
**Questions:** [GitHub Discussions](https://github.com/Benny-Lewis/super-roo/discussions)
**Compare to obra:** [obra/superpowers](https://github.com/obra/superpowers)

---

## Summary

The v2 redesign achieves **maximum fidelity** to obra/superpowers while maintaining all the benefits of the original SuperRoo implementation.

**Key changes:**
- 21 skill-modes (adapted from obra/superpowers)
- Skills compose via isolated subtasks
- Entry point mode for skill selection
- Same workflows, better structure

**Migration:** Update `.roomodes`, restart VS Code, start using!
