# super-roo

[![License: MPL-2.0](https://img.shields.io/badge/License-MPL--2.0-blue.svg)](https://www.mozilla.org/MPL/2.0/)

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
- [RooCode extension](https://marketplace.visualstudio.com/items?itemName=RooCline.roo-cline) installed

### Global Installation (Recommended - Works Across All Projects)

SuperRoo can be installed globally so it's available in **every project** you work on, or per-project if you prefer isolation.

**Step 1: Clone the repository**
```bash
git clone https://github.com/Benny-Lewis/super-roo.git
cd super-roo
```

**Step 2: Copy files to RooCode's global settings directory**

Run these commands **from inside the super-roo directory** (where you just cloned it):

**Windows (PowerShell or CMD):**
```powershell
# Copy custom modes configuration
copy .roomodes "$env:APPDATA\Code\User\roo-code-settings\customModes.json"

# Copy rules and commands directories
xcopy /E /I .roo\rules "$env:APPDATA\Code\User\roo-code-settings\rules"
xcopy /E /I .roo\commands "$env:APPDATA\Code\User\roo-code-settings\commands"
```

**macOS/Linux:**
```bash
# Create settings directory if it doesn't exist
mkdir -p ~/.config/Code/User/roo-code-settings

# Copy custom modes configuration
cp .roomodes ~/.config/Code/User/roo-code-settings/customModes.json

# Copy rules and commands directories
cp -r .roo/rules ~/.config/Code/User/roo-code-settings/
cp -r .roo/commands ~/.config/Code/User/roo-code-settings/
```

**What these paths mean:**
- **Windows:** `%APPDATA%\Code\User\roo-code-settings\` (typically `C:\Users\YourName\AppData\Roaming\Code\User\roo-code-settings\`)
- **macOS/Linux:** `~/.config/Code/User/roo-code-settings/`

These are **global configuration directories** - once installed here, SuperRoo skill-modes will be available in **every project** you open in VS Code.

**Step 3: Restart VS Code**

Close and reopen VS Code completely (not just reload window).

**Step 4: Verify installation**

Open any project in VS Code and check:

**Expected results:**
- **Modes dropdown** shows 20 SuperRoo skill-modes:
  - using-superpowers, test-driven-development, systematic-debugging, brainstorming, etc.

- **Slash commands** work in RooCode chat:
  - `/tdd` - Test-driven development
  - `/debug` - Systematic debugging
  - `/brainstorm` - Design refinement
  - `/write-plan` - Create implementation plan
  - `/execute-plan` - Execute plan with TDD
  - `/review` - Request code review
  - `/finish` - Complete development branch

**Step 5: Recommended - Configure Auto-Approval**

Speed up SuperRoo's read-heavy investigation workflows by auto-approving read-only operations.

Add this to your VS Code `settings.json` (`Ctrl+,` or `Cmd+,` → "Open Settings (JSON)"):

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

---

### Project-Specific Installation (Advanced)

If you want SuperRoo **only in a specific project** (not globally), or want to override global settings for one project:

```bash
# In your project directory
cp /path/to/super-roo/.roomodes .
cp -r /path/to/super-roo/.roo .
```

**When to use project-specific installation:**
- Testing SuperRoo modifications before global deployment
- Project has custom skill-modes or rules
- Working with a team that doesn't use SuperRoo globally
- Want to use a different version of SuperRoo for a specific project

**Note:** Project-specific installation (`.roomodes` and `.roo/` in project root) **overrides** global settings for that project only.

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
