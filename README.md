# super-roo

**Superpowers methodology ported to RooCode**

A battle-tested development methodology featuring TDD, systematic debugging, rigorous code review, and disciplined workflows - now available for RooCode.

---

## What is super-roo?

super-roo brings the [superpowers](https://github.com/obra/superpowers) development methodology from Claude Code to RooCode. It provides:

- 🔴 **Test-Driven Development (TDD)** - RED-GREEN-REFACTOR cycle enforced
- 🔍 **Systematic Debugging** - 4-phase root-cause investigation
- 👁️ **Automatic Code Review** - Review after every task completion
- 📐 **Rigorous Planning** - Design before implementation
- ✅ **Verification-First** - Evidence before completion claims

---

## Features

### 4 Custom RooCode Modes

1. **superpowers-code** - TDD-driven implementation with auto-review
2. **superpowers-debug** - Systematic root-cause debugging
3. **superpowers-architect** - Design, planning, and documentation
4. **superpowers-review** - Rigorous code review (read-only)

### Core Principles (Non-Negotiable)

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

1. **Clone this repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/super-roo.git
   cd super-roo
   ```

2. **Copy files to RooCode settings:**

   **Windows:**
   ```bash
   # Copy modes file
   copy .roomodes %APPDATA%\Code\User\roo-code-settings\customModes.json

   # Copy rules and commands
   xcopy /E /I .roo\rules %APPDATA%\Code\User\roo-code-settings\rules
   xcopy /E /I .roo\commands %APPDATA%\Code\User\roo-code-settings\commands
   ```

   **macOS/Linux:**
   ```bash
   # Copy modes file
   cp .roomodes ~/.config/Code/User/roo-code-settings/customModes.json

   # Copy rules and commands
   cp -r .roo/rules ~/.config/Code/User/roo-code-settings/
   cp -r .roo/commands ~/.config/Code/User/roo-code-settings/
   ```

3. **Restart VS Code**

4. **Verify installation:**
   - Open VS Code
   - RooCode should now show superpowers modes available
   - Check for: superpowers-code, superpowers-debug, superpowers-architect, superpowers-review

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

1. **Start a session** - RooCode defaults to superpowers-architect mode
2. **Plan your work** - Brainstorm, create implementation plan
3. **Switch to code mode** - Implement with TDD
4. **Auto-review triggers** - After each task completion
5. **Address feedback** - Fix issues with TDD
6. **Finish branch** - Verify, merge, clean up

### Example Workflow

```
User: "Add user authentication"

superpowers-architect mode:
→ Brainstorm design (Socratic questions)
→ Write implementation plan (5 TDD-based tasks)

superpowers-code mode:
→ Task 1: Write failing test → Implement → Refactor
→ Auto-review triggers → Address feedback
→ Task 2: Write failing test → Implement → Refactor
→ Auto-review triggers → Address feedback
→ ... (repeat for all tasks)

superpowers-architect mode:
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

## Comparison to Original Superpowers

| Aspect | Original (Claude Code) | super-roo (RooCode) |
|--------|------------------------|---------------------|
| Core methodology | TDD, debugging, review | Identical ✅ |
| Skill count | 20 skills | 20 skills ✅ |
| Workflows | All workflows | All preserved ✅ |
| Sub-agents | Independent | Hierarchical (MCP upgrade planned) |
| Auto-discipline | Behavioral | Auto-trigger review ⭐ |
| Mode bypass protection | N/A | Global rule ⭐ |

**Fidelity:** 95% - Core methodology identical, some optimizations

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
- **super-roo port** - Bringing rigorous development methodology to RooCode

---

## Support

- **Issues:** [GitHub Issues](https://github.com/YOUR_USERNAME/super-roo/issues)
- **Discussions:** [GitHub Discussions](https://github.com/YOUR_USERNAME/super-roo/discussions)
- **Original superpowers:** [obra/superpowers](https://github.com/obra/superpowers)

---

**Start building with discipline. Start using super-roo.** 🚀
