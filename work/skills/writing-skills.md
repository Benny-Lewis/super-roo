# Writing Skills

**Create new skills with TDD approach to process documentation**

## Overview

This skill guides you through creating new skill-modes for SuperRoo, applying TDD principles to process documentation.

## When to Use

- Creating a new workflow that doesn't fit existing skills
- Adapting a pattern from another project
- Documenting a team-specific practice
- Contributing new skills upstream

## Workflow

### 1. Identify the Need

**What problem does this skill solve?**
- What workflow is currently painful?
- What mistakes happen repeatedly?
- What knowledge needs to be codified?

**Define success criteria:**
- What does "using this skill correctly" look like?
- What mistakes should it prevent?
- How will you know it works?

### 2. Research Existing Patterns

- Check if similar skill already exists
- Look for patterns in current skills
- Review obra/superpowers for inspiration
- Study the problem domain

### 3. Draft the Skill

**Structure:**
```markdown
# Skill Name

**When to use:** Clear trigger conditions

## Overview
Brief description

## Workflow
Step-by-step process

## Red Flags (Don't Do This)
Common mistakes to avoid

## Tool Requirements
- Groups: [read, edit, command]

## Skill Composition
- What skills does this invoke?

## Completion Criteria
- How do you know you're done?
```

**Key elements:**
- Clear trigger ("When to use")
- Step-by-step workflow
- Red flags (anti-patterns)
- Tool requirements
- Composition patterns

### 4. Test the Skill

**Method:** Use `testing-skills-with-subagents`
- Spawn agent with the skill
- Give it a realistic scenario
- Observe if it follows the skill correctly
- Identify where it rationalizes around the process

**Iterate:**
- Add clarifications where agent got confused
- Strengthen language where agent rationalized
- Add examples where process wasn't clear

### 5. Integrate into SuperRoo

**Create the mode:**
```yaml
- slug: {skill-name}
  name: {Skill Display Name}
  description: "{Short description}"
  roleDefinition: |
    # SKILL: {SKILL NAME}

    [Skill content here]

    ## COMMUNICATION AND TOOL USAGE

    ALWAYS communicate before using tools:
    - Explain what you're about to do
    - Use tools
    - Explain results
  groups:
    - {read/edit/command}
```

**Add slash command (if commonly used):**
```markdown
---
description: {Skill description}
---

Switch to {skill-name} mode and apply its methodology.
```

### 6. Document and Share

- Add to skill catalog in `using-superpowers`
- Update documentation
- Consider contributing upstream (use `sharing-skills`)

## Example: Creating "API Design Review" Skill

**1. Need:** Team keeps making inconsistent API decisions

**2. Research:** Review existing APIs, REST best practices, GraphQL patterns

**3. Draft:**
```markdown
# API Design Review

**When to use:** Before implementing any new API endpoint

## Workflow
1. Review API contract
2. Check consistency with existing APIs
3. Verify error handling
4. Validate security
...
```

**4. Test:** Spawn agent with skill, give it API design task, observe

**5. Iterate:** Agent forgot to check auth → Add "Security checklist" section

**6. Integrate:** Add as mode, create `/api-review` command

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- Spawns: `testing-skills-with-subagents` to validate skill
- May spawn: `sharing-skills` to contribute upstream

## Completion Criteria
- Skill drafted with all key sections
- Tested with subagent
- Integrated into SuperRoo
- Documented
