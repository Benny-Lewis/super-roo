# Super-Roo Sync Phase 3: Remaining Skills

**Prerequisite:** Phase 2 merged

## Scope

### Skills to Sync (9 total)

| Skill | Changes |
|-------|---------|
| `systematic-debugging` | Rationalizations table, partner signals |
| `brainstorming` | CSO optimization |
| `dispatching-parallel-agents` | Dot diagrams, real examples |
| `executing-plans` | Announcements, when-to-stop |
| `receiving-code-review` | Forbidden responses, YAGNI check |
| `using-git-worktrees` | Announce pattern, common mistakes |
| `writing-plans` | Header template with sub-skill reference |
| `using-superpowers` | Merge invocation rules with catalog |
| `requesting-code-review` | Add subagent dispatch pattern |

> **Note:** All Phase 3 skill names match their mode slugs exactly. Verify by checking `.roomodes` before syncing.

### Glossary

| Term | Meaning |
|------|---------|
| Rationalizations table | Table mapping common developer excuses to proper debugging actions |
| Partner signals | Indicators from pairing partner (e.g., confusion, disagreement) that should trigger behavior changes |
| CSO optimization | Clarity-Speed-Outcome framework for selecting brainstorming approach |
| Dot diagrams | Graphviz-style diagrams showing agent dispatch flow |
| Announcements | Explicit user-facing status messages before/after major actions |
| When-to-stop | Criteria for determining when plan execution is complete |
| Forbidden responses | Phrases the mode must never output (e.g., defensive justifications) |
| YAGNI check | "You Aren't Gonna Need It" - validation that changes don't add unnecessary features |
| Announce pattern | Consistent format for notifying user of state changes |
| Common mistakes | Documented pitfalls to avoid (anti-patterns) |
| Header template | Standard structure for plan document headers |
| Sub-skill reference | Cross-reference to related skills within skill documentation |
| Invocation rules | Patterns for when/how to trigger a skill |
| Real examples | Concrete code/scenario demonstrations rather than abstract descriptions |
| Subagent dispatch pattern | Template for spawning child agents to handle subtasks |

## Source Files

Location: `C:\Users\blewis\.claude\plugins\cache\superpowers-marketplace\superpowers\<VERSION>\skills\`

Find current version:
```bash
ls -d ~/.claude/plugins/cache/superpowers-marketplace/superpowers/*/ | sort -V | tail -1
```

## Transformation Rules

| Superpowers | Super-Roo |
|-------------|-----------|
| `superpowers:{skill}` | `{skill-slug}` mode |
| `Task tool` | `new_task()` |
| `Skill tool` | Mode switch |

### Transformation Examples

**Skill references:**
```markdown
# Before (Superpowers)
See superpowers:writing-plans for template details.

# After (Super-Roo)
See [writing-plans] mode for template details.
```

**Spawning subagents:**
```markdown
# Before (Superpowers)
Use the Task tool to spawn a code-review agent with subagent_type="code-review".

# After (Super-Roo)
Use new_task() to delegate to a specialist:
<new_task>
<mode>code-review</mode>
<message>Review the authentication changes in auth.py</message>
</new_task>
```

**Invoking skills:**
```markdown
# Before (Superpowers)
Invoke the Skill tool with skill="commit" to create a commit.

# After (Super-Roo)
Switch to [git-committing] mode:
<switch_mode>
<mode_slug>git-committing</mode_slug>
<reason>User requested a commit</reason>
</switch_mode>
```

## Super-Roo Exclusives (DO NOT MODIFY)

These exist only in super-roo - preserve as-is:
- `condition-based-waiting`
- `defense-in-depth`
- `root-cause-tracing`
- `sharing-skills`
- `testing-anti-patterns`
- `testing-skills-with-subagents`

**Conflict resolution:** When upstream changes conflict with Super-Roo exclusives, preserve the Super-Roo version and document the divergence.

## Current Mode Inventory (21 modes)

Phase 3 syncs updates to existing skills; no new modes are added.

| # | Mode Slug |
|---|-----------|
| 1 | `brainstorming` |
| 2 | `code-reviewer` |
| 3 | `condition-based-waiting` |
| 4 | `defense-in-depth` |
| 5 | `dispatching-parallel-agents` |
| 6 | `executing-plans` |
| 7 | `finishing-a-development-branch` |
| 8 | `receiving-code-review` |
| 9 | `requesting-code-review` |
| 10 | `root-cause-tracing` |
| 11 | `sharing-skills` |
| 12 | `subagent-driven-development` |
| 13 | `systematic-debugging` |
| 14 | `test-driven-development` |
| 15 | `testing-anti-patterns` |
| 16 | `testing-skills-with-subagents` |
| 17 | `using-git-worktrees` |
| 18 | `using-superpowers` |
| 19 | `verification-before-completion` |
| 20 | `writing-plans` |
| 21 | `writing-skills` |

## Pre-Sync Backup

Before starting, create a backup for comparison:
```bash
cp .roomodes .roomodes.pre-phase3
```

## Validation

### Validation Steps

- [x] **YAML validates:**
  ```bash
  python -c "import yaml; yaml.safe_load(open('.roomodes', encoding='utf-8'))"
  ```

- [x] **Mode definitions valid:** Each mode has `slug`, `name`, `roleDefinition`, `customInstructions`
  ```bash
  python -c "
  import yaml
  modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
  required = {'slug', 'name', 'roleDefinition', 'customInstructions'}
  for m in modes:
      missing = required - set(m.keys())
      if missing: print(f\"{m.get('slug','?')}: missing {missing}\")
  print('Validation complete')
  "
  ```

- [x] **All 21 modes present:**
  ```bash
  python -c "import yaml; print('Mode count:', len(yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']))"
  ```

- [x] **No duplicate slugs:**
  ```bash
  python -c "
  import yaml
  from collections import Counter
  modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
  dupes = [s for s,c in Counter(m['slug'] for m in modes).items() if c>1]
  print('Duplicates:', dupes or 'None')
  "
  ```

- [x] **Skill content transformed:** No `superpowers:`, `Task tool`, or `Skill tool` references
  ```bash
  grep -E "superpowers:|Task tool|Skill tool" .roomodes || echo "Clean - no forbidden references"
  ```

- [x] **Exclusives unchanged:** Diff Super-Roo exclusives against pre-sync backup
  ```bash
  # Compare sections for: condition-based-waiting, defense-in-depth,
  # root-cause-tracing, sharing-skills, testing-anti-patterns, testing-skills-with-subagents
  diff .roomodes.pre-phase3 .roomodes | head -50
  ```
