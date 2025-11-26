# Contributing to SuperRoo

Thank you for your interest in contributing to SuperRoo! This project ports the battle-tested [superpowers](https://github.com/obra/superpowers) development methodology to RooCode.

---

## How to Contribute

### Reporting Issues

Found a bug or have a feature request?

1. Check [existing issues](https://github.com/Benny-Lewis/super-roo/issues) first
2. If not found, [create a new issue](https://github.com/Benny-Lewis/super-roo/issues/new)
3. Include:
   - Clear description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - RooCode version
   - Relevant logs or screenshots

---

### Suggesting Enhancements

Have ideas for improving SuperRoo?

1. [Open an issue](https://github.com/Benny-Lewis/super-roo/issues/new) with the "enhancement" label
2. Describe:
   - The problem you're trying to solve
   - Your proposed solution
   - Why it aligns with SuperRoo's core methodology

---

## Development Workflow

**IMPORTANT:** When contributing to SuperRoo, use SuperRoo! Practice what we preach.

### Setting Up

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/super-roo.git
   cd super-roo
   ```

2. **Install SuperRoo locally** (project-specific):
   ```bash
   # Files are already in the repo
   # Just open in RooCode and the modes will be available
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

### Making Changes

Use the SuperRoo methodology for all contributions:

#### For New Features:
1. **Start with using-superpowers mode** (entry point)
2. Use `/brainstorm` or select **brainstorming mode** to refine the design
3. Use `/write-plan` or select **writing-plans mode** to create implementation plan
4. Use `/execute-plan` or select **executing-plans mode**
5. Subtasks will use **test-driven-development mode** (TDD enforced)
6. Auto-review will trigger after each task

**Or go direct:**
1. Select **test-driven-development mode** for implementing
2. Write test first (RED), implement (GREEN), refactor
3. Auto-review triggers automatically

#### For Bug Fixes:
1. **Use systematic-debugging mode** (or `/debug`)
2. Follow the 4-phase debugging framework:
   - Phase 1: Root cause investigation
   - Phase 2: Pattern analysis
   - Phase 3: Hypothesis and testing
   - Phase 4: Implementation (with TDD)
3. Auto-review will trigger after fix

#### For Documentation:
1. **Use brainstorming or writing-plans mode** for substantial docs
2. Or any mode for minor doc changes
3. Request review if significant (use **requesting-code-review mode** or `/review`)

---

### Pull Request Process

1. **Ensure all tests pass**
   ```bash
   # Run verification appropriate to your changes
   ```

2. **Update documentation**
   - Update README.md if adding features
   - Update docs/ARCHITECTURE.md if changing architecture
   - Add/update examples if helpful

3. **Follow commit message conventions**
   ```
   Add feature: brief description

   Longer explanation of what changed and why.

   - Bullet points for details
   - Reference issues: Fixes #123
   ```

4. **Create Pull Request**
   - Clear title describing the change
   - Reference related issues
   - Describe what was changed and why
   - Include test results

5. **Code Review**
   - Address feedback from reviewers
   - Make requested changes
   - Update PR description if scope changes

---

## Code Standards

### Core Principles (Non-Negotiable)

All contributions MUST follow SuperRoo's core principles:

- 🔴 **NO CODE WITHOUT FAILING TEST FIRST**
- ✅ **NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION**
- 🔍 **ROOT CAUSE INVESTIGATION BEFORE FIXES**
- 👁️ **REVIEW EARLY, REVIEW OFTEN**

### Mode-Specific Guidelines

When modifying modes:

1. **Preserve core methodology** - Don't weaken the discipline
2. **Test with subagents** - Ensure modes work as intended
3. **Document changes** - Update ARCHITECTURE.md
4. **Maintain fidelity** - Stay true to original superpowers when possible

---

## Types of Contributions Needed

### High Priority

- **Bug fixes** - Modes not working as expected
- **Documentation improvements** - Clarify confusing sections
- **Examples** - Real-world usage examples
- **Testing** - Verify modes work in different scenarios

### Welcome Contributions

- **New slash commands** - Additional helpful workflows
- **Mode enhancements** - Improve existing modes (without weakening discipline)
- **Installation scripts** - Easier setup process
- **Integration guides** - How to use with specific frameworks

### Not Accepting

- **Weakening discipline** - Removing TDD, verification, or review requirements
- **Mode bypass features** - Anything that makes it easier to skip SuperRoo modes
- **Anti-patterns** - Changes that encourage bad practices

---

## Community Guidelines

### Be Respectful

- Treat all contributors with respect
- Assume good intentions
- Provide constructive feedback
- Focus on the code, not the person

### Technical Rigor

SuperRoo values **technical rigor over politeness**:
- Point out issues clearly and directly
- "This has a race condition" not "Maybe consider..."
- Question assumptions when appropriate
- Never performatively agreeable

But always be respectful and professional.

---

## Questions?

- **General questions:** [Open a discussion](https://github.com/Benny-Lewis/super-roo/discussions)
- **Bug reports:** [Open an issue](https://github.com/Benny-Lewis/super-roo/issues)
- **Original superpowers:** See [obra/superpowers](https://github.com/obra/superpowers)

---

## License

By contributing to SuperRoo, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for helping make SuperRoo better!** 🦘
