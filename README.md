# super-roo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Rigorous development discipline for RooCode.**

Enforced TDD, systematic debugging, and automatic code review—the [superpowers](https://github.com/obra/superpowers) methodology adapted for RooCode.

---

## What You Get

**Four Custom Modes:**
- **superroo-code** - TDD-driven implementation with automatic code review after every task
- **superroo-debug** - 4-phase systematic debugging with root-cause tracing
- **superroo-architect** - Design refinement, comprehensive planning, git worktree workflows
- **superroo-review** - Rigorous code review (read-only, structural constraints)

**20 Embedded Skills** from original superpowers:
- **test-driven-development** - RED-GREEN-REFACTOR cycle enforced
- **systematic-debugging** - 4-phase root-cause investigation framework
- **brainstorming** - Socratic design refinement with incremental validation
- **verification-before-completion** - Evidence before any completion claims
- **requesting-code-review** - Automatic review triggers after task completion
- **testing-anti-patterns** - Prevents testing mock behavior, test-only methods
- **root-cause-tracing** - Backward tracing through call stack to original trigger
- **condition-based-waiting** - Eliminates flaky tests with proper async handling
- **defense-in-depth** - Multi-layer validation makes bugs structurally impossible
- **writing-plans** - Comprehensive implementation plans assuming zero context
- **executing-plans** - Batch execution with review checkpoints
- **using-git-worktrees** - Isolated workspace setup with safety verification
- **finishing-a-development-branch** - Complete development with merge/PR/cleanup options
- **subagent-driven-development** - Per-task subagent dispatch with review gates
- **sharing-skills** - Contribute improvements back upstream
- [Full details in ARCHITECTURE.md](docs/ARCHITECTURE.md)

**Automatic Quality Gates:**
- Auto-triggered code review after every task completion (no asking permission)
- Structural constraints enforced by RooCode (read-only review mode, docs-only architect)
- Global rule prevents bypassing SuperRoo modes for convenience
- Explicit role switching (conductor vs player) prevents implementation confusion

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
   - Modes dropdown shows: superroo-code, superroo-debug, superroo-architect, superroo-review
   - Global rule loaded (enforces methodology discipline)

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

1. **Start a session** - RooCode defaults to superroo-architect mode
2. **Plan your work** - Brainstorm, create implementation plan
3. **Switch to code mode** - Implement with TDD
4. **Auto-review triggers** - After each task completion
5. **Address feedback** - Fix issues with TDD
6. **Finish branch** - Verify, merge, clean up

### Example Workflow

```
User: "Add user authentication"

superroo-architect mode:
→ Brainstorm design (Socratic questions)
→ Write implementation plan (5 TDD-based tasks)

superroo-code mode:
→ Task 1: Write failing test → Implement → Refactor
→ Auto-review triggers → Address feedback
→ Task 2: Write failing test → Implement → Refactor
→ Auto-review triggers → Address feedback
→ ... (repeat for all tasks)

superroo-architect mode:
→ Finish branch (verify, create PR, cleanup)
```

---

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for complete technical details.

**Key design decisions:**

- **Fat modes with explicit orchestration** - Modes have both conductor and player roles
- **Auto-trigger code review** - Review is automatic after task completion
- **Structural constraints** - Read-only review, docs-only architect edit
- **Global rule** - Prevents mode bypass, establishes core principles
- **Hierarchical subtasks** - Uses RooCode's native `new_task` (future MCP upgrade planned)

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
| Skill count | 20 skills | 20 skills ✅ |
| Workflows | All workflows | All preserved ✅ |
| Sub-agents | Independent | Hierarchical (MCP upgrade planned) |
| Auto-discipline | Behavioral | Auto-trigger review ⭐ |
| Mode bypass protection | N/A | Global rule ⭐ |

**Fidelity:** 95% - Core methodology identical, some optimizations for RooCode platform

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
