# Sharing Skills

**Contribute improvements back upstream to obra/superpowers or SuperRoo**

## Overview

Guide the process of branching, committing, pushing, and creating pull requests to contribute skills back to the upstream repository.

## When to Use

- Created a valuable new skill others could use
- Fixed/improved an existing skill
- Found and fixed bugs in skill definitions
- Want to contribute back to the community

## Prerequisites

Before sharing:
- ✅ Skill tested with `testing-skills-with-subagents`
- ✅ Skill proven useful in real work
- ✅ Skill follows project patterns
- ✅ Documentation is clear and complete

## Workflow

### 1. Verify Quality

**Check your skill:**
- Does it solve a real problem?
- Is it tested and proven?
- Does it follow existing patterns?
- Is documentation clear?
- Are there examples?

**Red flags (don't contribute yet):**
- Skill is untested
- Skill is project-specific
- Documentation is sparse
- Haven't used it in real work

### 2. Choose Upstream

**SuperRoo (this project):**
- RooCode-specific improvements
- RooCode mode definitions
- SuperRoo workflow enhancements

**obra/superpowers:**
- General methodology improvements
- Claude Code skills
- Platform-agnostic workflows

### 3. Create Branch

```bash
git checkout -b contribute/{skill-name}
```

Or use `using-git-worktrees` for isolated workspace:
```bash
git worktree add ../super-roo-{skill-name} -b contribute/{skill-name}
```

### 4. Make Changes

**For new skill:**
- Add skill file: `work/skills/{skill-name}.md`
- Add mode definition in `.roomodes`
- Add to skill catalog in `using-superpowers`
- Add slash command if appropriate
- Update documentation

**For skill improvement:**
- Make targeted changes
- Test with `testing-skills-with-subagents`
- Update related documentation

### 5. Commit

```bash
git add {files}
git commit -m "{Clear description of contribution}"
```

**Good commit messages:**
- "Add API design review skill"
- "Fix TDD skill: prevent 'sketch first' rationalization"
- "Improve brainstorming: add YAGNI enforcement"

**Bad commit messages:**
- "Updates"
- "Fix stuff"
- "WIP"

### 6. Push and Create PR

```bash
git push -u origin contribute/{skill-name}
```

**Create pull request:**
- Clear title describing contribution
- Description explaining:
  - What problem this solves
  - How it was tested
  - Examples of usage
- Link to any related issues

**PR template:**
```markdown
## Problem
[What problem does this solve?]

## Solution
[How does this skill address it?]

## Testing
[How was this tested? Include examples]

## Examples
[Show skill in action]
```

### 7. Respond to Review

Use `receiving-code-review` skill:
- Address feedback with technical rigor
- Don't performatively agree
- Question assumptions
- Iterate until approved

### 8. Celebrate

🎉 You've contributed to the community!

## Example: Contributing "API Design Review"

**1. Quality check:**
- ✅ Used for 5 API reviews
- ✅ Caught 3 security issues
- ✅ Tested with subagents
- ✅ Documentation complete

**2. Upstream:** SuperRoo (RooCode-specific)

**3. Branch:** `contribute/api-design-review`

**4. Changes:**
- Add `work/skills/api-design-review.md`
- Add mode in `.roomodes`
- Add to skill catalog
- Add `/api-review` command
- Update README

**5. Commit:** "Add API design review skill"

**6. Push and PR:**
- Title: "Add API design review skill for consistent API decisions"
- Description: Links to examples, explains testing
- Screenshots of skill in action

**7. Review:** Address feedback, iterate

**8. Merged!** 🎉

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- May use: `using-git-worktrees` for isolated workspace
- May use: `receiving-code-review` for PR feedback
- May use: `testing-skills-with-subagents` before contributing

## Completion Criteria
- Branch created
- Changes committed
- PR opened
- Feedback addressed (if any)
- Contribution merged or ready for review
