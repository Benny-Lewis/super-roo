# Skill Inventory - Current SuperRoo Modes

## Current Mode Structure

### superroo-review (lines 2-230)
**Embedded Skills:**
1. requesting-code-review (the entire mode)

**Tool Access:** `groups: [read, command]` (read-only)

---

### superroo-code (lines 231-668)
**Embedded Skills:**
1. test-driven-development (line 327)
2. testing-anti-patterns (line 386)
3. verification-before-completion (line 451)
4. requesting-code-review (line 495)
5. condition-based-waiting (line 529)
6. defense-in-depth (line 573)

**Tool Access:** `groups: [read, edit, command]`

---

### superroo-debug (lines 669-1196)
**Embedded Skills:**
1. systematic-debugging (line 770)
2. root-cause-tracing (line 931)
3. test-driven-development (line 1005)
4. testing-anti-patterns (line 1027)
5. verification-before-completion (line 1055)
6. requesting-code-review (line 1080)
7. condition-based-waiting (line 1100)
8. defense-in-depth (line 1135)

**Tool Access:** `groups: [read, edit, command]`

---

### superroo-architect (lines 1197-1650)
**Embedded Skills:**
1. brainstorming (line 1293)
2. writing-plans (line 1336)
3. executing-plans (line 1406)
4. using-git-worktrees (line 1449)
5. finishing-a-development-branch (line 1495)
6. subagent-driven-development (line 1532)
7. verification-before-completion (line 1573)
8. requesting-code-review (line 1598)

**Tool Access:** `groups: [read, edit, command]` + `fileRegex: "**/*.md"`

---

## Target: 20 Skill-Modes

Based on obra/superpowers, we need these 20 skills:

### ✅ Already Extracted (9 unique skills)
1. test-driven-development
2. testing-anti-patterns
3. verification-before-completion
4. requesting-code-review
5. condition-based-waiting
6. defense-in-depth
7. systematic-debugging
8. root-cause-tracing
9. brainstorming
10. writing-plans
11. executing-plans
12. using-git-worktrees
13. finishing-a-development-branch
14. subagent-driven-development

### ❌ Missing Skills (need to create from scratch)
15. **using-superpowers** - Entry point mode (from superpowers skill)
16. **receiving-code-review** - How to process review feedback
17. **dispatching-parallel-agents** - Spawn multiple independent investigations
18. **writing-skills** - Create new skills with TDD
19. **testing-skills-with-subagents** - Validate skills work under pressure
20. **sharing-skills** - Contribute improvements upstream

---

## Extraction Strategy

### Phase 1: Extract Existing Skills (14 skills)
For each embedded skill:
1. Extract line ranges from .roomodes
2. Save to `work/skills/{skill-name}.md`
3. Document tool requirements
4. Identify composition patterns

### Phase 2: Create Missing Skills (6 skills)
For skills not in current SuperRoo:
1. Research from obra/superpowers repo
2. Create new skill content
3. Define tool requirements
4. Define composition patterns

---

## Next Steps

1. ✅ Skill inventory complete
2. ⏭️ Extract 14 existing skills from .roomodes
3. ⏭️ Create 6 missing skills
4. ⏭️ Identify skill dependencies
