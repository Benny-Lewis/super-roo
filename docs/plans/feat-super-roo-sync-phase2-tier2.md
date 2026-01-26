# Super-Roo Sync Phase 2: Tier 2 Skills

**Prerequisite:** Phase 1 MVP merged

## Scope

3 skills with significant updates:

| Skill | Key Changes |
|-------|-------------|
| `subagent-driven-development` | **Two-stage review** (spec then quality), prompt templates, 1 flowchart (mermaid) |
| `finishing-a-development-branch` | Bash commands, quick reference table, Red Flags |
| `verification-before-completion` | Expanded tables (capped at 5 rows each) |

## Source Files

Location: `C:\Users\blewis\.claude\plugins\cache\superpowers-marketplace\superpowers\4.1.0\skills\`

## Implementation Order

Execute in this order to manage dependencies:

1. **verification-before-completion** (foundational, referenced by others)
2. **finishing-a-development-branch** (uses verification concepts)
3. **subagent-driven-development** (builds on both)

## Implementation

### 1. verification-before-completion
- Expand Common Failures table (3 → **5** items, capped)
- Expand Rationalization table (3 → **5** items, capped)
- Add explicit "When To Apply" list
- Add "Why This Matters" section
- Remove marketing/promotional language - keep operational only

### 2. finishing-a-development-branch
- Add "Announce at start" pattern
- Add detailed bash commands for each option
- Add Quick Reference table (4 options × 5 columns)
- Consolidate Common Mistakes into Red Flags section (no separate section)
- Add Integration section

### 3. subagent-driven-development
- Add two-stage review process (spec compliance THEN code quality)
- Prompt templates: **inline** into skill file (not separate files)
- Add **1** process flowchart (convert Graphviz → Mermaid)
- Consolidate all warnings into single Red Flags section
- Remove "Advantages/Cost" marketing language
- Adapt: `TodoWrite` → `new_task()` per translation table below

### TodoWrite → new_task() Translation

| Superpowers Pattern | Super-Roo Equivalent |
|---------------------|----------------------|
| `TodoWrite` with all tasks | `new_task()` for each task |
| Mark task complete in TodoWrite | `attempt_completion` with result |
| TodoRead to check status | Check task context directly |

## Validation

- [x] All .roomodes YAML validates (use yamllint or manual check)
- [x] Each mode frontmatter validates
- [ ] Test subagent dispatch for subagent-driven-development
- [ ] Test /finish command with all 4 options
- [ ] Test verification-before-completion gates completion claims
- [ ] Regression: existing Phase 1 skills still work
- [ ] Bash commands work on Windows (Git Bash)
