# Super-Roo Sync Phase 3: Remaining Skills

**Prerequisite:** Phase 2 merged

## Scope

### Tier 3: Moderate Updates (7 skills)

| Skill | Changes |
|-------|---------|
| `systematic-debugging` | Rationalizations table, partner signals |
| `brainstorming` | CSO optimization |
| `dispatching-parallel-agents` | Dot diagrams, real examples |
| `executing-plans` | Announcements, when-to-stop |
| `receiving-code-review` | Forbidden responses, YAGNI check |
| `using-git-worktrees` | Announce pattern, common mistakes |
| `writing-plans` | Header template with sub-skill reference |

### Tier 4: Structural Updates (2 skills)

| Skill | Changes |
|-------|---------|
| `using-superpowers` | Merge invocation rules with catalog |
| `requesting-code-review` | Add subagent dispatch pattern |

## Source Files

Location: `C:\Users\blewis\.claude\plugins\cache\superpowers-marketplace\superpowers\4.1.0\skills\`

## Transformation Rules

| Superpowers | Super-Roo |
|-------------|-----------|
| `superpowers:{skill}` | `{skill-slug}` mode |
| `Task tool` | `new_task()` |
| `Skill tool` | Mode switch |

## Super-Roo Exclusives (DO NOT MODIFY)

These exist only in super-roo - preserve as-is:
- `condition-based-waiting`
- `defense-in-depth`
- `root-cause-tracing`
- `sharing-skills`
- `testing-anti-patterns`
- `testing-skills-with-subagents`

## Validation

- [ ] YAML validates
- [ ] All 20 original modes still work
- [ ] Final mode count: 21
