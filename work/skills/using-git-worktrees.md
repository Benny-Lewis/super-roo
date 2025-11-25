# Using Git Worktrees

### Skill 4: Using Git Worktrees

      **When:** Starting feature work needing isolation

      **Directory Selection Priority:**

      1. **Check Existing:**
         ```bash
         ls -d .worktrees 2>/dev/null     # Preferred
         ls -d worktrees 2>/dev/null      # Alternative
         ```
         If found: Use it. If both: `.worktrees` wins.

      2. **Check CLAUDE.md:**
         ```bash
         grep -i "worktree.*director" CLAUDE.md 2>/dev/null
         ```
         If preference specified: Use it.

      3. **Ask User:**
         If no directory and no CLAUDE.md preference:
         ```
         No worktree directory found. Where should I create worktrees?
         1. .worktrees/ (project-local, hidden)
         2. ~/.config/superroo/worktrees/<project>/ (global)
         ```

      **Safety Verification (project-local only):**
      ```bash
      # MUST verify .gitignore
      grep -q "^\.worktrees/$" .gitignore || grep -q "^worktrees/$" .gitignore
      ```
      If NOT in .gitignore:
      - Add it immediately
      - Commit change
      - Then proceed

      **Creation Steps:**
      1. Detect project name
      2. Create worktree with new branch
      3. Run project setup (auto-detect: npm install, cargo build, etc.)
      4. Verify clean baseline (run tests)
      5. Report location and status

      ---

---

## Tool Requirements
- Groups: `['read', 'edit', 'command']`

## Skill Composition
- No automatic composition

## Completion Criteria
- (To be defined based on skill content)
