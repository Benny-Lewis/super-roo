# super-roo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Rigorous development discipline for RooCode.**

Enforced TDD, systematic debugging, and automatic code review—the [superpowers](https://github.com/obra/superpowers) methodology adapted for RooCode.

---

## What You Get

**20 Skill-Modes** (1:1 mapping to [obra/superpowers](https://github.com/obra/superpowers)):

**Entry Point:**
- **using-superpowers** - Entry point that helps you select the right skill

**Development Skills (7):**
- **test-driven-development** - RED-GREEN-REFACTOR cycle enforced
- **testing-anti-patterns** - Prevents testing mock behavior, test-only methods
- **verification-before-completion** - Evidence before any completion claims
- **condition-based-waiting** - Eliminates flaky tests with proper async handling
- **defense-in-depth** - Multi-layer validation makes bugs structurally impossible
- **receiving-code-review** - Process review feedback with technical rigor
- **requesting-code-review** - Perform rigorous code review (read-only mode)

**Debugging Skills (3):**
- **systematic-debugging** - 4-phase root-cause investigation framework
- **root-cause-tracing** - Backward tracing through call stack to original trigger
- **dispatching-parallel-agents** - Spawn multiple independent investigations concurrently

**Planning & Architecture Skills (6):**
- **brainstorming** - Socratic design refinement with incremental validation
- **writing-plans** - Comprehensive implementation plans assuming zero context
- **executing-plans** - Batch execution with review checkpoints
- **subagent-driven-development** - Per-task subagent dispatch with review gates
- **using-git-worktrees** - Isolated workspace setup with safety verification
- **finishing-a-development-branch** - Complete development with merge/PR/cleanup options

**Meta & Workflow Skills (4):**
- **writing-skills** - Create new skills with TDD
- **testing-skills-with-subagents** - Validate skills work under pressure
- **sharing-skills** - Contribute improvements back upstream
- **using-superpowers** (listed above)

[Full details in ARCHITECTURE.md](docs/ARCHITECTURE.md)

**Automatic Quality Gates:**
- Auto-triggered code review after every task completion (no asking permission)
- Structural constraints enforced by RooCode (read-only review mode)
- Skills compose via isolated subtasks (using RooCode's `new_task`)
- Each skill has clear completion criteria and return summaries

**Core Principles (Non-Negotiable):**
- 🔴 **NO CODE WITHOUT FAILING TEST FIRST**
- ✅ **NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION**
- 🔍 **ROOT CAUSE INVESTIGATION BEFORE FIXES**
- 👁️ **REVIEW EARLY, REVIEW OFTEN**

---

## Installation

### Prerequisites

- [VS Code](https://code.visualstudio.com/)
- [RooCode extension](https://github.com/RooCodeInc/Roo-Code) installed

### Global Installation (All Projects)

**Step 1: Clone the repository**
```bash
git clone https://github.com/Benny-Lewis/super-roo.git
cd super-roo
```

**Step 2: Copy files to RooCode settings**

Run these commands **from inside the super-roo directory** (where you just cloned it):

**Windows:**
```bash
copy .roomodes %APPDATA%\Code\User\roo-code-settings\customModes.json
xcopy /E /I .roo\rules %APPDATA%\Code\User\roo-code-settings\rules
xcopy /E /I .roo\commands %APPDATA%\Code\User\roo-code-settings\commands
```

**macOS/Linux:**
```bash
cp .roomodes ~/.config/Code/User/roo-code-settings/customModes.json
cp -r .roo/rules ~/.config/Code/User/roo-code-settings/
cp -r .roo/commands ~/.config/Code/User/roo-code-settings/
```

**Note:** These commands copy files from the current directory (`.roomodes`, `.roo/*`) to your RooCode settings folder. No modifications needed—just run them as-is.

**Step 3: Restart VS Code**

**Step 4: Verify installation**
   - Restart VS Code
   - Open RooCode mode selector

   **Expected result:**
   - Modes dropdown shows 20 skill-modes (using-superpowers, test-driven-development, etc.)
   - Slash commands work: `/tdd`, `/debug`, `/brainstorm`, `/write-plan`, `/execute-plan`, `/review`

**Step 5: Recommended - Configure Auto-Approval**

Speed up SuperRoo's read-heavy investigation workflows by auto-approving read-only operations.

Add this to your VS Code settings.json (`Ctrl+,` → "Open Settings (JSON)"):

```json
"roo-cline.autoApprovalSettings": {
  "read_file": true,
  "list_files": true,
  "search_files": true,
  "list_code_definition_names": true
}
```

**What this does:**
- ✅ Auto-approves: Reading files, listing files, searching, and code definition lookups
- 🛡️ Still requires approval: File edits, command execution, and all write operations

This significantly speeds up debugging and code review workflows while maintaining safety for destructive operations.

### Project-Specific Installation

To use super-roo in a single project:

```bash
# In your project directory
cp /path/to/super-roo/.roomodes .
cp -r /path/to/super-roo/.roo .
```

---

## Usage

### Quick Start

**Option 1: Let SuperRoo Choose**
1. **Start with using-superpowers mode** - Entry point that analyzes your request
2. **SuperRoo selects appropriate skill** - Automatically spawns the right mode
3. **Skills auto-compose** - TDD triggers review, brainstorm offers to create plan, etc.

**Option 2: Direct Skill Selection**
1. **Use slash commands** - Quick access: `/tdd`, `/debug`, `/brainstorm`
2. **Or select mode directly** - Choose from 20 skill-modes in dropdown
3. **Skills auto-compose** - Each skill knows when to invoke others

### Example Workflows

**Feature Implementation:**
```
User: "Add user authentication"

using-superpowers mode:
→ Analyzes request → Selects brainstorming mode
→ Spawns: brainstorming

brainstorming mode:
→ Refines design through Socratic questions
→ Presents 2-3 approaches with trade-offs
→ User approves design
→ Offers: writing-plans

writing-plans mode:
→ Creates detailed plan with TDD tasks
→ Offers: executing-plans

executing-plans mode:
→ Spawns: test-driven-development (Task 1)
  → RED-GREEN-REFACTOR
  → Auto-spawns: requesting-code-review
  → Returns to executing-plans
→ Spawns: test-driven-development (Task 2)
  → (repeat pattern)
→ All tasks complete
```

**Quick Bug Fix:**
```
User: "/debug - tests failing for empty email"

systematic-debugging mode:
→ Investigates root cause (4-phase framework)
→ Creates failing test (RED)
→ Implements fix (GREEN)
→ Auto-spawns: requesting-code-review
→ Review feedback → Addresses issues
→ Complete
```

---

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for complete technical details.

**Key design decisions:**

- **One mode per skill** - 20 skill-modes with 1:1 mapping to obra/superpowers
- **Skill composition via new_task** - Skills invoke other skills with isolated contexts
- **Auto-trigger code review** - Review is automatic after task completion
- **Structural constraints** - Read-only review mode enforced by RooCode
- **Entry point mode** - using-superpowers helps select the right skill
- **90% fidelity to obra/superpowers** - Maximum compatibility with original methodology

---

## Philosophy

SuperRoo enforces discipline through structure, not suggestions:

- **Discipline over convenience** - The methodology enforces good practices, it doesn't suggest them
- **Evidence before claims** - "Fixed" requires verification output, not confidence or assumptions
- **Test-first always** - If you didn't watch the test fail, it proves nothing about behavior
- **Root cause over symptoms** - Quick patches mask underlying issues and create more bugs
- **Review catches issues early** - Automatic review after every task prevents compound problems
- **Structural constraints** - Read-only review mode makes violations impossible, not just discouraged

---

## Comparison to Original Superpowers

| Aspect | Original (Claude Code) | super-roo (RooCode) |
|--------|------------------------|---------------------|
| Core methodology | TDD, debugging, review | Identical ✅ |
| Skill count | 20 skills | 20 skill-modes ✅ |
| Skill files | Separate files | Modes (embedded) 🟡 |
| On-demand loading | Load when needed | Only active mode loaded ✅ |
| Skill mental model | Skill-centric | Skill-centric ✅ |
| Agent independence | Isolated (Task tool) | Isolated (new_task) ✅ |
| Skill composability | Skills invoke skills | Modes invoke modes ✅ |
| Auto skill detection | Automatic | Entry point mode 🟡 |
| Workflows | All workflows | All preserved ✅ |
| Auto-discipline | Behavioral | Structural (auto-trigger) ⭐ |

**Fidelity:** 90% - Core methodology identical, maximum compatibility with obra/superpowers

---

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## License

MIT License - see [LICENSE](LICENSE) file

---

## Credits

- **Original superpowers** by [Jesse Vincent](https://github.com/obra) - [github.com/obra/superpowers](https://github.com/obra/superpowers)
- **RooCode** by [RooCode Inc](https://github.com/RooCodeInc) - [github.com/RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code)

---

## Support

- **Issues:** [GitHub Issues](https://github.com/Benny-Lewis/super-roo/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Benny-Lewis/super-roo/discussions)
- **Original superpowers:** [obra/superpowers](https://github.com/obra/superpowers)

---

**Start building with discipline. Start using super-roo.** 🚀
