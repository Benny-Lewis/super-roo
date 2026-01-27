# Skill Sync Prevention Strategies

Prevention strategies for common problems when syncing skills from Superpowers to Super-Roo.

**Based on issues encountered during Phase 2 and Phase 3 syncs.**

---

## Pre-Sync Checklist

Complete these steps **before** making any changes to `.roomodes`:

### 1. Environment Verification

```bash
# Verify Python has yaml module
python -c "import yaml; print('YAML module OK')"

# Verify current directory
pwd
# Should be: C:\Users\blewis\dev\super-roo

# Verify .roomodes exists and is valid
python -c "import yaml; yaml.safe_load(open('.roomodes', encoding='utf-8')); print('Current .roomodes is valid')"
```

### 2. Create Backup

```bash
# Create timestamped backup
cp .roomodes ".roomodes.backup-$(date +%Y%m%d-%H%M%S)"

# Or create named backup for the phase
cp .roomodes .roomodes.pre-phase3
```

### 3. Inventory Current Modes

```bash
# List all current mode slugs with count
python -c "
import yaml
modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
print(f'Total modes: {len(modes)}')
print('Mode slugs:')
for i, m in enumerate(modes, 1):
    print(f'  {i}. {m[\"slug\"]}')
"
```

**Save this output!** Compare after sync to detect unintended changes.

### 4. Identify Source Files

```bash
# Find latest Superpowers version
ls -d ~/.claude/plugins/cache/superpowers-marketplace/superpowers/*/ | sort -V | tail -1

# List skills to sync
ls ~/.claude/plugins/cache/superpowers-marketplace/superpowers/*/skills/
```

### 5. Review Super-Roo Exclusives

These modes exist **only** in Super-Roo and must **never** be modified during sync:

| Slug | Purpose |
|------|---------|
| `condition-based-waiting` | Flaky test elimination |
| `defense-in-depth` | Multi-layer validation |
| `root-cause-tracing` | Backward call stack tracing |
| `sharing-skills` | Upstream contribution |
| `testing-anti-patterns` | Mock/test-only method prevention |
| `testing-skills-with-subagents` | Skill validation under pressure |

---

## Validation Commands

Run these **after every change** to `.roomodes`:

### Quick Validation (Run Frequently)

```bash
# YAML syntax check with UTF-8 encoding
python -c "import yaml; yaml.safe_load(open('.roomodes', encoding='utf-8')); print('YAML: OK')"
```

### Full Validation Suite

```bash
# 1. YAML validates with proper encoding
python -c "import yaml; yaml.safe_load(open('.roomodes', encoding='utf-8')); print('1. YAML syntax: OK')"

# 2. Mode count matches expected
python -c "
import yaml
modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
expected = 21
actual = len(modes)
status = 'OK' if actual == expected else f'MISMATCH (expected {expected})'
print(f'2. Mode count: {actual} - {status}')
"

# 3. All required fields present
python -c "
import yaml
modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
required = {'slug', 'name', 'roleDefinition'}
issues = []
for m in modes:
    missing = required - set(m.keys())
    if missing:
        issues.append(f\"{m.get('slug', '?')}: missing {missing}\")
print('3. Required fields:', 'OK' if not issues else '\\n   '.join(['ISSUES:'] + issues))
"

# 4. No duplicate slugs
python -c "
import yaml
from collections import Counter
modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
dupes = [s for s, c in Counter(m['slug'] for m in modes).items() if c > 1]
print('4. Duplicate slugs:', dupes if dupes else 'None (OK)')
"

# 5. No forbidden references (Superpowers-specific syntax)
grep -E "superpowers:|Task tool|Skill tool|TodoWrite|TodoRead" .roomodes && echo "5. Forbidden refs: FOUND - needs cleanup" || echo "5. Forbidden refs: None (OK)"

# 6. All exclusives unchanged (compare with backup)
echo "6. Exclusives check: Run diff against backup for exclusives"
```

### Single-Command Validation Script

Save as `validate-roomodes.py`:

```python
#!/usr/bin/env python3
"""Validate .roomodes file for Super-Roo sync."""
import yaml
import sys
from collections import Counter

def main():
    print("=== .roomodes Validation ===\n")
    errors = []

    # 1. Load with UTF-8
    try:
        with open('.roomodes', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        print("[OK] YAML syntax valid")
    except Exception as e:
        print(f"[FAIL] YAML error: {e}")
        sys.exit(1)

    modes = data.get('customModes', [])

    # 2. Mode count
    expected = 21
    actual = len(modes)
    if actual == expected:
        print(f"[OK] Mode count: {actual}")
    else:
        print(f"[WARN] Mode count: {actual} (expected {expected})")
        errors.append(f"Mode count mismatch: {actual} vs {expected}")

    # 3. Required fields
    required = {'slug', 'name', 'roleDefinition'}
    for m in modes:
        missing = required - set(m.keys())
        if missing:
            errors.append(f"{m.get('slug', '?')}: missing {missing}")
    print(f"[{'OK' if not errors else 'FAIL'}] Required fields")

    # 4. Duplicates
    slugs = [m['slug'] for m in modes]
    dupes = [s for s, c in Counter(slugs).items() if c > 1]
    if dupes:
        errors.append(f"Duplicate slugs: {dupes}")
        print(f"[FAIL] Duplicate slugs: {dupes}")
    else:
        print("[OK] No duplicate slugs")

    # 5. Forbidden references
    with open('.roomodes', encoding='utf-8') as f:
        content = f.read()
    forbidden = ['superpowers:', 'Task tool', 'Skill tool', 'TodoWrite', 'TodoRead']
    found = [f for f in forbidden if f in content]
    if found:
        errors.append(f"Forbidden references: {found}")
        print(f"[FAIL] Forbidden references: {found}")
    else:
        print("[OK] No forbidden references")

    # Summary
    print(f"\n=== Summary ===")
    print(f"Modes: {actual}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nIssues found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\nAll checks passed!")
        sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Common Pitfalls to Avoid

### Pitfall 1: Windows Encoding Errors

**Problem:** Python fails to read `.roomodes` on Windows due to encoding.

**Symptom:**
```
UnicodeDecodeError: 'cp1252' codec can't decode byte...
```

**Prevention:**
```python
# ALWAYS specify encoding='utf-8'
yaml.safe_load(open('.roomodes', encoding='utf-8'))

# NEVER use this (uses system default encoding)
yaml.safe_load(open('.roomodes'))
```

**Fix if encountered:**
```bash
# Convert file to UTF-8 if needed
iconv -f CP1252 -t UTF-8 .roomodes > .roomodes.utf8
mv .roomodes.utf8 .roomodes
```

### Pitfall 2: Phantom Mode Inventory

**Problem:** Plan documents list modes that don't exist or miss modes that do.

**Symptom:** Mode count in docs doesn't match actual `.roomodes` count.

**Prevention:**
1. **Always generate inventory from source of truth:**
   ```bash
   # Generate current inventory - don't copy from old docs
   python -c "
   import yaml
   modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
   print(f'Mode count: {len(modes)}')
   for i, m in enumerate(modes, 1):
       print(f'| {i} | \`{m[\"slug\"]}\` |')
   "
   ```

2. **Cross-check before syncing:**
   - Does the skill exist in `.roomodes`? (update)
   - Or is it new? (add)

3. **After sync, regenerate inventory** - don't manually edit counts.

### Pitfall 3: Incomplete Transformation Rules

**Problem:** Generic rules without concrete examples lead to inconsistent transforms.

**Prevention:** Document transformations with before/after examples.

**Good documentation:**
```markdown
### Skill References

**Before (Superpowers):**
```
See superpowers:writing-plans for template details.
Use the Skill tool with skill="commit".
```

**After (Super-Roo):**
```
See [writing-plans] mode for template details.
Switch to [git-committing] mode.
```
```

**Bad documentation:**
```markdown
### Skill References
Convert superpowers:{skill} to {skill-slug} mode.
```

### Pitfall 4: YAML Multi-line String Corruption

**Problem:** Editing roleDefinition breaks YAML structure.

**Symptom:**
```
yaml.scanner.ScannerError: mapping values are not allowed here
```

**Prevention:**
1. **Use `|` for multi-line strings:**
   ```yaml
   roleDefinition: |
     Content here...
     More content...
   ```

2. **Watch indentation** - content must be indented consistently under the key.

3. **Escape special characters:**
   - Backslashes in code blocks: `\\` not `\`
   - Quotes in strings: use opposite quote type or escape

4. **Validate after every edit:**
   ```bash
   python -c "import yaml; yaml.safe_load(open('.roomodes', encoding='utf-8'))"
   ```

### Pitfall 5: Overwriting Super-Roo Exclusives

**Problem:** Accidentally modifying Super-Roo-only skills during sync.

**Prevention:**
1. **Mark exclusives clearly in plan docs**
2. **Check before modifying any mode:**
   ```python
   EXCLUSIVES = {
       'condition-based-waiting',
       'defense-in-depth',
       'root-cause-tracing',
       'sharing-skills',
       'testing-anti-patterns',
       'testing-skills-with-subagents',
   }

   # Before editing
   if mode_slug in EXCLUSIVES:
       print(f"WARNING: {mode_slug} is a Super-Roo exclusive - DO NOT MODIFY")
   ```

3. **After sync, diff exclusives against backup:**
   ```bash
   # Extract and compare exclusive modes
   for slug in condition-based-waiting defense-in-depth root-cause-tracing sharing-skills testing-anti-patterns testing-skills-with-subagents; do
     echo "=== $slug ==="
     diff <(python -c "
   import yaml
   modes = yaml.safe_load(open('.roomodes.backup', encoding='utf-8'))['customModes']
   m = next((x for x in modes if x['slug'] == '$slug'), None)
   print(m['roleDefinition'] if m else 'NOT FOUND')
   ") <(python -c "
   import yaml
   modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
   m = next((x for x in modes if x['slug'] == '$slug'), None)
   print(m['roleDefinition'] if m else 'NOT FOUND')
   ")
   done
   ```

### Pitfall 6: Forgetting Graphviz-to-Mermaid Conversion

**Problem:** Graphviz DOT syntax left in roleDefinition (won't render in RooCode).

**Detection:**
```bash
# Find any Graphviz syntax
grep -E "digraph|->.*\[label=" .roomodes && echo "Found Graphviz - needs conversion"
```

**Conversion rules:**

| Graphviz | Mermaid |
|----------|---------|
| `digraph name {` | `flowchart TD` |
| `[shape=diamond]` | `{text}` |
| `[shape=box]` | `[text]` |
| `A -> B` | `A --> B` |
| `A -> B [label="yes"]` | `A -->\|yes\| B` |
| Quoted node names | Single-letter IDs (A, B, C) |

---

## Test Cases for Verifying Sync Success

### Test 1: YAML Validity

```bash
# Must pass without errors
python -c "import yaml; yaml.safe_load(open('.roomodes', encoding='utf-8'))"
echo "Exit code: $?"  # Should be 0
```

**Pass criteria:** Exit code 0, no output.

### Test 2: Mode Count Unchanged

```bash
# Before sync (save this)
python -c "import yaml; print(len(yaml.safe_load(open('.roomodes.backup', encoding='utf-8'))['customModes']))"

# After sync (should match or document why different)
python -c "import yaml; print(len(yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']))"
```

**Pass criteria:** Count matches expected (21 for current Super-Roo).

### Test 3: No Forbidden References

```bash
# All should return empty
grep "superpowers:" .roomodes
grep "Task tool" .roomodes
grep "Skill tool" .roomodes
grep "TodoWrite" .roomodes
grep "TodoRead" .roomodes
```

**Pass criteria:** All grep commands return nothing (exit code 1).

### Test 4: Exclusives Unchanged

```bash
# For each exclusive, verify content hash matches
for slug in condition-based-waiting defense-in-depth root-cause-tracing sharing-skills testing-anti-patterns testing-skills-with-subagents; do
  before=$(python -c "
import yaml, hashlib
modes = yaml.safe_load(open('.roomodes.backup', encoding='utf-8'))['customModes']
m = next((x for x in modes if x['slug'] == '$slug'), None)
print(hashlib.md5(m['roleDefinition'].encode()).hexdigest() if m else 'MISSING')
")
  after=$(python -c "
import yaml, hashlib
modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
m = next((x for x in modes if x['slug'] == '$slug'), None)
print(hashlib.md5(m['roleDefinition'].encode()).hexdigest() if m else 'MISSING')
")
  if [ "$before" = "$after" ]; then
    echo "[OK] $slug unchanged"
  else
    echo "[FAIL] $slug was modified!"
  fi
done
```

**Pass criteria:** All exclusives show "unchanged".

### Test 5: Key Content Present

For each synced skill, verify key sections exist:

```bash
# Example: Check systematic-debugging has rationalizations table
python -c "
import yaml
modes = yaml.safe_load(open('.roomodes', encoding='utf-8'))['customModes']
m = next((x for x in modes if x['slug'] == 'systematic-debugging'), None)
content = m['roleDefinition']
checks = [
    ('Rationalizations table', 'Rationalization' in content or 'rationalization' in content),
    ('Partner signals', 'partner' in content.lower()),
]
for name, passed in checks:
    print(f\"[{'OK' if passed else 'FAIL'}] {name}\")
"
```

**Pass criteria:** All expected content checks pass.

### Test 6: Mermaid Diagrams Render

1. Copy a mermaid diagram from `.roomodes`
2. Paste into https://mermaid.live/
3. Verify it renders correctly

**Pass criteria:** Diagram renders without syntax errors.

### Test 7: Functional Test (Manual)

1. Open VS Code with Super-Roo
2. Select a synced mode from dropdown
3. Give it a task matching its purpose
4. Verify behavior matches skill intent

**Pass criteria:** Mode behaves as documented.

---

## Recovery Procedures

### If YAML Is Corrupted

```bash
# Restore from backup
cp .roomodes.backup .roomodes

# Or restore from git
git checkout .roomodes
```

### If Wrong Mode Modified

```bash
# Extract specific mode from backup
python -c "
import yaml
# Load backup
backup = yaml.safe_load(open('.roomodes.backup', encoding='utf-8'))
current = yaml.safe_load(open('.roomodes', encoding='utf-8'))

# Find mode in backup
slug = 'condition-based-waiting'  # Change as needed
backup_mode = next((m for m in backup['customModes'] if m['slug'] == slug), None)

# Replace in current
for i, m in enumerate(current['customModes']):
    if m['slug'] == slug:
        current['customModes'][i] = backup_mode
        break

# Save
with open('.roomodes', 'w', encoding='utf-8') as f:
    yaml.dump(current, f, default_flow_style=False, allow_unicode=True)
print(f'Restored {slug} from backup')
"
```

### If Count Mismatch

1. Generate inventory from both files
2. Find missing/extra modes
3. Either restore from backup or document the change

---

## Quick Reference Card

```
PRE-SYNC:
  [ ] Backup: cp .roomodes .roomodes.backup
  [ ] Inventory: python -c "import yaml; ..."
  [ ] Identify sources: ls ~/.claude/.../skills/
  [ ] Review exclusives list

DURING SYNC:
  [ ] Use encoding='utf-8' always
  [ ] Validate after each edit
  [ ] Convert Graphviz to Mermaid
  [ ] Transform: superpowers:{x} -> [{x}] mode
  [ ] Transform: Task tool -> new_task()
  [ ] Skip exclusives (6 modes)

POST-SYNC:
  [ ] Full validation suite
  [ ] Compare mode count
  [ ] Verify no forbidden refs
  [ ] Diff exclusives vs backup
  [ ] Manual smoke test
```

---

## References

- [SKILL-SYNC.md](./SKILL-SYNC.md) - Main sync procedure guide
- [Phase 2 Plan](./plans/feat-super-roo-sync-phase2-tier2.md)
- [Phase 3 Plan](./plans/feat-super-roo-sync-phase3-remaining.md)
