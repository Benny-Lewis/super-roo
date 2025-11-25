#!/usr/bin/env python3
"""
Generate .roomodes file from skill files
"""

from pathlib import Path
import yaml

def read_skill(skill_name):
    """Read a skill markdown file and extract content"""
    skill_path = Path('work/skills') / f'{skill_name}.md'
    with open(skill_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the metadata sections at the end
    if '---\n\n## Tool Requirements' in content:
        content = content.split('---\n\n## Tool Requirements')[0]
    
    return content.strip()

def get_tool_groups(skill_name):
    """Determine tool groups for a skill"""
    # Read-only review
    if skill_name == 'requesting-code-review':
        return ['read', 'command']
    
    # Docs-only (planning skills)
    if skill_name in ['brainstorming', 'writing-plans']:
        return ['read', 'edit', 'command']
    
    # Default: full access
    return ['read', 'edit', 'command']

def get_file_regex(skill_name):
    """Determine fileRegex constraint if any"""
    if skill_name in ['brainstorming', 'writing-plans']:
        return "**/*.md"
    return None

def create_mode_definition(skill_name, skill_slug, description):
    """Create a mode definition dict"""
    skill_content = read_skill(skill_name)
    tool_groups = get_tool_groups(skill_name)
    file_regex = get_file_regex(skill_name)
    
    # Create role definition
    role_def = f"""# SKILL: {skill_name.replace('-', ' ').upper()}

{skill_content}

---

## COMMUNICATION AND TOOL USAGE

**ALWAYS communicate before using tools:**
- Explain what you're about to do BEFORE making function calls
- Output text to communicate with the user (user sees your text, not raw function calls)
- NEVER use bash echo or code comments as means to communicate
- Example:
  - ❌ BAD: [immediately calls Read tool without explanation]
  - ✅ GOOD: "Let me check the implementation..." [then calls Read tool]

**Use TodoWrite for complex tasks:**
- Create todos when task has 3+ distinct steps
- Update status: pending → in_progress → completed
- Mark tasks complete IMMEDIATELY after finishing (don't batch)
- Keep exactly ONE task in_progress at a time
- Don't use for simple single-step tasks

**Tool usage patterns:**
- Read files in parallel when gathering context
- Explain findings after reading
- Show command output when verifying claims
"""
    
    mode = {
        'slug': skill_slug,
        'name': skill_name.replace('-', ' ').title(),
        'description': description,
        'roleDefinition': role_def,
        'whenToUse': f"Use this mode when you need to: {description.lower()}",
        'groups': tool_groups
    }
    
    if file_regex:
        mode['fileRegex'] = file_regex
    
    return mode

# Define all 20 skills with their metadata
skills = [
    # Entry point
    ('using-superpowers', 'using-superpowers', 'Entry point - helps you select the right skill'),
    
    # Development skills
    ('test-driven-development', 'test-driven-development', 'Implement features using RED-GREEN-REFACTOR'),
    ('testing-anti-patterns', 'testing-anti-patterns', 'Prevent testing mocks and test-only methods'),
    ('verification-before-completion', 'verification-before-completion', 'Evidence before any completion claims'),
    ('condition-based-waiting', 'condition-based-waiting', 'Eliminate flaky tests with proper async handling'),
    ('defense-in-depth', 'defense-in-depth', 'Multi-layer validation makes bugs structurally impossible'),
    ('receiving-code-review', 'receiving-code-review', 'Process review feedback with technical rigor'),
    ('requesting-code-review', 'requesting-code-review', 'Perform rigorous code review'),
    
    # Debugging skills
    ('systematic-debugging', 'systematic-debugging', '4-phase root-cause debugging framework'),
    ('root-cause-tracing', 'root-cause-tracing', 'Backward tracing through call stack to original trigger'),
    ('dispatching-parallel-agents', 'dispatching-parallel-agents', 'Spawn multiple independent investigations concurrently'),
    
    # Planning & Architecture skills
    ('brainstorming', 'brainstorming', 'Socratic design refinement with incremental validation'),
    ('writing-plans', 'writing-plans', 'Comprehensive implementation plans assuming zero context'),
    ('executing-plans', 'executing-plans', 'Batch execution with review checkpoints'),
    ('subagent-driven-development', 'subagent-driven-development', 'Per-task subagents with review gates'),
    ('using-git-worktrees', 'using-git-worktrees', 'Isolated workspace setup with safety verification'),
    ('finishing-a-development-branch', 'finishing-a-development-branch', 'Complete development work (merge/PR/cleanup)'),
    
    # Meta & Workflow skills
    ('writing-skills', 'writing-skills', 'Create new skills with TDD'),
    ('testing-skills-with-subagents', 'testing-skills-with-subagents', 'Validate skills work under pressure'),
    ('sharing-skills', 'sharing-skills', 'Contribute improvements upstream'),
]

# Generate modes
modes = []
for skill_name, skill_slug, description in skills:
    mode = create_mode_definition(skill_name, skill_slug, description)
    modes.append(mode)

# Write .roomodes file
output = {'customModes': modes}

with open('.roomodes.new', 'w', encoding='utf-8') as f:
    yaml.dump(output, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=1000)

print(f"✅ Generated .roomodes.new with {len(modes)} skill-modes")
print("\nNext steps:")
print("1. Review .roomodes.new")
print("2. If looks good: mv .roomodes .roomodes.old && mv .roomodes.new .roomodes")
