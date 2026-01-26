# Super-Roo Sync Phase 2: Tier 2 Skills

**Prerequisite:** Phase 1 MVP merged

## Scope

3 skills with significant updates:

| Skill | Key Changes |
|-------|-------------|
| `subagent-driven-development` | **Two-stage review** (spec then quality), prompt templates, flowchart |
| `finishing-a-development-branch` | Bash commands, quick reference table, common mistakes |
| `verification-before-completion` | Expanded tables (3→7 failures, 3→8 rationalizations) |

## Source Files

Location: `C:\Users\blewis\.claude\plugins\cache\superpowers-marketplace\superpowers\4.1.0\skills\`

## Implementation

### subagent-driven-development
- Add two-stage review process (spec compliance THEN code quality)
- Embed prompt templates: implementer, spec-reviewer, code-quality-reviewer
- Add process flowchart
- Add Red Flags including review order enforcement
- Adapt: `Task tool` → `new_task()`

### finishing-a-development-branch
- Add "Announce at start" pattern
- Add detailed bash commands for each option
- Add Quick Reference table (4 options × 5 columns)
- Add Common Mistakes section
- Add Integration section

### verification-before-completion
- Expand Common Failures table (3 → 7 items)
- Expand Rationalization table (3 → 8 items)
- Add explicit "When To Apply" list
- Add "Why This Matters" section

## Validation

- [ ] YAML validates
- [ ] Test subagent dispatch works
- [ ] Test /finish command
