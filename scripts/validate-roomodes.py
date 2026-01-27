#!/usr/bin/env python3
"""
Validate .roomodes file for Super-Roo sync.

Usage:
    python scripts/validate-roomodes.py
    python scripts/validate-roomodes.py --backup .roomodes.backup

Exit codes:
    0 - All checks passed
    1 - Validation errors found
"""
import yaml
import sys
import hashlib
import argparse
from collections import Counter
from pathlib import Path

# Super-Roo exclusive modes (never modified during sync)
EXCLUSIVES = {
    'condition-based-waiting',
    'defense-in-depth',
    'root-cause-tracing',
    'sharing-skills',
    'testing-anti-patterns',
    'testing-skills-with-subagents',
}

# Forbidden references (Superpowers-specific syntax)
FORBIDDEN = [
    'superpowers:',
    'Task tool',
    'Skill tool',
    'TodoWrite',
    'TodoRead',
]


def load_roomodes(filepath: str) -> dict:
    """Load .roomodes with UTF-8 encoding."""
    with open(filepath, encoding='utf-8') as f:
        return yaml.safe_load(f)


def check_yaml_syntax(filepath: str) -> tuple[bool, str]:
    """Check if file is valid YAML."""
    try:
        load_roomodes(filepath)
        return True, "YAML syntax valid"
    except yaml.YAMLError as e:
        return False, f"YAML error: {e}"
    except UnicodeDecodeError as e:
        return False, f"Encoding error (use UTF-8): {e}"


def check_mode_count(data: dict, expected: int = 21) -> tuple[bool, str]:
    """Check mode count matches expected."""
    modes = data.get('customModes', [])
    actual = len(modes)
    if actual == expected:
        return True, f"Mode count: {actual}"
    else:
        return False, f"Mode count: {actual} (expected {expected})"


def check_required_fields(data: dict) -> tuple[bool, str]:
    """Check all modes have required fields."""
    modes = data.get('customModes', [])
    required = {'slug', 'name', 'roleDefinition'}
    issues = []

    for m in modes:
        missing = required - set(m.keys())
        if missing:
            issues.append(f"  {m.get('slug', '?')}: missing {missing}")

    if issues:
        return False, "Missing required fields:\n" + "\n".join(issues)
    return True, "All required fields present"


def check_duplicates(data: dict) -> tuple[bool, str]:
    """Check for duplicate slugs."""
    modes = data.get('customModes', [])
    slugs = [m['slug'] for m in modes]
    dupes = [s for s, c in Counter(slugs).items() if c > 1]

    if dupes:
        return False, f"Duplicate slugs: {dupes}"
    return True, "No duplicate slugs"


def check_forbidden_refs(filepath: str) -> tuple[bool, str]:
    """Check for forbidden Superpowers-specific references."""
    import re

    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    found = []

    # Check for superpowers:{skill-name} pattern (skill references)
    # But not just "superpowers:" in documentation context
    superpowers_refs = re.findall(r'superpowers:\w+', content)
    if superpowers_refs:
        found.append(f"superpowers:* skill refs: {superpowers_refs[:5]}")

    # Check other forbidden patterns
    other_forbidden = ['Task tool', 'Skill tool', 'TodoWrite', 'TodoRead']
    for f_pattern in other_forbidden:
        if f_pattern in content:
            found.append(f_pattern)

    if found:
        return False, f"Forbidden references found: {found}"
    return True, "No forbidden references"


def check_exclusives_unchanged(current_file: str, backup_file: str) -> tuple[bool, str]:
    """Check that exclusive modes haven't been modified."""
    if not Path(backup_file).exists():
        return True, f"Exclusives check skipped (no backup: {backup_file})"

    try:
        current = load_roomodes(current_file)
        backup = load_roomodes(backup_file)
    except Exception as e:
        return False, f"Error loading files for comparison: {e}"

    current_modes = {m['slug']: m for m in current.get('customModes', [])}
    backup_modes = {m['slug']: m for m in backup.get('customModes', [])}

    modified = []
    for slug in EXCLUSIVES:
        curr = current_modes.get(slug, {}).get('roleDefinition', '')
        back = backup_modes.get(slug, {}).get('roleDefinition', '')

        if hashlib.md5(curr.encode()).hexdigest() != hashlib.md5(back.encode()).hexdigest():
            modified.append(slug)

    if modified:
        return False, f"Exclusives were modified: {modified}"
    return True, "All exclusives unchanged"


def check_mermaid_syntax(data: dict) -> tuple[bool, str]:
    """Check for leftover Graphviz syntax."""
    modes = data.get('customModes', [])
    graphviz_indicators = ['digraph ', '-> ', '[shape=']
    issues = []

    for m in modes:
        content = m.get('roleDefinition', '')
        # Skip if it's clearly explaining Graphviz conversion
        if 'Graphviz' in content and 'Mermaid' in content:
            continue

        for indicator in graphviz_indicators:
            if indicator in content and 'mermaid' not in content.lower()[:content.find(indicator) if content.find(indicator) > 0 else 0]:
                # Check if it's in a conversion example (has both -> and -->)
                if indicator == '-> ' and '-->' in content:
                    continue
                issues.append(f"  {m['slug']}: may contain Graphviz syntax ({indicator.strip()})")
                break

    if issues:
        return False, "Possible Graphviz syntax (should be Mermaid):\n" + "\n".join(issues)
    return True, "No Graphviz syntax detected"


def main():
    parser = argparse.ArgumentParser(description='Validate .roomodes file')
    parser.add_argument('file', nargs='?', default='.roomodes', help='Path to .roomodes file')
    parser.add_argument('--backup', default='.roomodes.backup', help='Path to backup for comparison')
    parser.add_argument('--expected-count', type=int, default=21, help='Expected mode count (default: 21)')
    args = parser.parse_args()

    expected_count = args.expected_count

    print("=" * 50)
    print("Super-Roo .roomodes Validation")
    print("=" * 50)
    print(f"\nFile: {args.file}")
    print(f"Backup: {args.backup}")
    print()

    errors = []
    warnings = []

    # Check 1: YAML syntax
    passed, msg = check_yaml_syntax(args.file)
    print(f"[{'OK' if passed else 'FAIL'}] {msg}")
    if not passed:
        errors.append(msg)
        print("\nCannot continue - fix YAML syntax first")
        sys.exit(1)

    # Load data for remaining checks
    data = load_roomodes(args.file)

    # Check 2: Mode count
    passed, msg = check_mode_count(data, expected_count)
    print(f"[{'OK' if passed else 'WARN'}] {msg}")
    if not passed:
        warnings.append(msg)

    # Check 3: Required fields
    passed, msg = check_required_fields(data)
    print(f"[{'OK' if passed else 'FAIL'}] {msg}")
    if not passed:
        errors.append(msg)

    # Check 4: Duplicates
    passed, msg = check_duplicates(data)
    print(f"[{'OK' if passed else 'FAIL'}] {msg}")
    if not passed:
        errors.append(msg)

    # Check 5: Forbidden references
    passed, msg = check_forbidden_refs(args.file)
    print(f"[{'OK' if passed else 'FAIL'}] {msg}")
    if not passed:
        errors.append(msg)

    # Check 6: Exclusives unchanged
    passed, msg = check_exclusives_unchanged(args.file, args.backup)
    print(f"[{'OK' if passed else 'FAIL'}] {msg}")
    if not passed:
        errors.append(msg)

    # Check 7: Mermaid syntax
    passed, msg = check_mermaid_syntax(data)
    print(f"[{'OK' if passed else 'WARN'}] {msg}")
    if not passed:
        warnings.append(msg)

    # Summary
    print()
    print("=" * 50)
    print("Summary")
    print("=" * 50)

    modes = data.get('customModes', [])
    print(f"\nModes found: {len(modes)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("\n[ERRORS - Must Fix]")
        for e in errors:
            for line in e.split('\n'):
                print(f"  {line}")

    if warnings:
        print("\n[WARNINGS - Review]")
        for w in warnings:
            for line in w.split('\n'):
                print(f"  {line}")

    if not errors and not warnings:
        print("\nAll checks passed!")

    print()

    # List all modes
    print("Mode inventory:")
    for i, m in enumerate(modes, 1):
        exclusive_marker = " (exclusive)" if m['slug'] in EXCLUSIVES else ""
        print(f"  {i:2}. {m['slug']}{exclusive_marker}")

    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
