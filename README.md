<!-- SPDX-License-Identifier: MIT -->

<div align="center">

<br>
<img src="assets/neenee_dp_2x.png" width="128">
<br>

# Neenee
### An elegant & scalable Discord bot which aces in robustness<br>✨ (and in doing chores :D) 🪄

[![Format](https://github.com/hitblast/Neenee/actions/workflows/formatting.yml/badge.svg)](https://github.com/hitblast/Neenee/actions/workflows/formatting.yml)
[![Lint](https://github.com/hitblast/Neenee/actions/workflows/linting.yml/badge.svg)](https://github.com/hitblast/Neenee/actions/workflows/linting.yml)

</div>

<br>

## 🔖 Table of Contents

- [Todo](#-todo)

- [Setup](#-setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Configuration](#configuration)

- [Usage](#-usage)
    - [Commands](#commands)

- [Contributing](#-contributing)
    - [Development Guide](#development-guide)
    - [Code of Conduct](#code-of-conduct)

<br>

## 📝 Todo

- [x] Setup project structure with [Poetry](https://python-poetry.org/)
- [ ] Setup basic bot infrastructure:
    - [x] Implement core class for managing the bot (neenee/bot.py)
    - [x] Add CLI-based interface within (neenee/cli.py)
    - [ ] Create a custom credential manager for handling bot secrets (for now, will improve later)
    - [ ] Centralize console-based error messages
    - [ ] Prepare a setup guideline within README.md
- [ ] Add cogs / extensions:
    - [x] Prepare a basic `dev` cog for monitoring the bot while in development
    - [ ] Decentralize the cogs system so that it can be scalable as needed
    - [ ] Implement a `moderation` cog for server moderation commands
    - [ ] Implement a `general` cog for normal commands
- [ ] Add advanced features (for now):
    - [ ] Improve the logging system and centralize it for universal access
- [ ] Chore tasks:
    - [ ] Improve the CLI with interactive prompts (backend is ready)