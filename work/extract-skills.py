#!/usr/bin/env python3
"""
Extract skills from .roomodes file into separate markdown files.
"""

import re
from pathlib import Path

def extract_skills():
    roomodes_path = Path(__file__).parent.parent / '.roomodes'
    skills_dir = Path(__file__).parent / 'skills'
    skills_dir.mkdir(exist_ok=True)

    with open(roomodes_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define skill patterns and their locations
    skills = [
        # From superroo-code
        ('test-driven-development', 327, 385, ['read', 'edit', 'command'], 'requesting-code-review'),
        ('testing-anti-patterns', 386, 450, ['read', 'edit', 'command'], None),
        ('verification-before-completion', 451, 494, ['read', 'edit', 'command'], None),
        ('requesting-code-review', 495, 528, ['read', 'command'], None),
        ('condition-based-waiting', 529, 572, ['read', 'edit', 'command'], None),
        ('defense-in-depth', 573, 668, ['read', 'edit', 'command'], None),

        # From superroo-debug
        ('systematic-debugging', 770, 930, ['read', 'edit', 'command'], 'requesting-code-review'),
        ('root-cause-tracing', 931, 1004, ['read', 'edit', 'command'], None),

        # From superroo-architect
        ('brainstorming', 1293, 1335, ['read', 'edit', 'command'], 'writing-plans'),
        ('writing-plans', 1336, 1405, ['read', 'edit', 'command'], 'executing-plans'),
        ('executing-plans', 1406, 1448, ['read', 'edit', 'command'], 'test-driven-development'),
        ('using-git-worktrees', 1449, 1494, ['read', 'edit', 'command'], None),
        ('finishing-a-development-branch', 1495, 1531, ['read', 'edit', 'command'], None),
        ('subagent-driven-development', 1532, 1572, ['read', 'edit', 'command'], 'test-driven-development'),
    ]

    lines = content.split('\n')

    for skill_name, start, end, tools, composes_with in skills:
        # Extract skill content
        skill_lines = lines[start-1:end]
        skill_content = '\n'.join(skill_lines)

        # Remove the "### Skill N:" header
        skill_content = re.sub(r'^### Skill \d+: .+?\n\n', '', skill_content, flags=re.MULTILINE)

        # Create markdown file
        md_content = f"""# {skill_name.replace('-', ' ').title()}

{skill_content.strip()}

---

## Tool Requirements
- Groups: `{tools}`

## Skill Composition
"""
        if composes_with:
            md_content += f"- Spawns: `{composes_with}`\n"
        else:
            md_content += "- No automatic composition\n"

        md_content += "\n## Completion Criteria\n"
        md_content += "- (To be defined based on skill content)\n"

        # Write to file
        output_path = skills_dir / f'{skill_name}.md'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✓ Extracted: {skill_name}")

    print(f"\n✅ Extracted {len(skills)} skills to {skills_dir}")

if __name__ == '__main__':
    extract_skills()
