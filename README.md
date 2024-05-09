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

- [Setup](#-setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [To-do List](#-to-do-list)
- [Contributing](#-contributing)
    - [Code of Conduct](./CODE_OF_CONDUCT.md)

<br>

## 🔨 Setup

### Prerequisites

- [**Python 3.12**](https://python.org/) or higher
- **[Poetry](https://python-poetry.org/)** for managing dependencies
- **[Git](https://git-scm.com/)** for version control

### Installation

1. Clone the repository and navigate to it: 
    ```sh
    $ git clone https://github.com/hitblast/Neenee.git && cd Neenee
    ```

2. Setup a virtual environment with Python and activate:
    ```sh
    $ python -m venv venv
    $ source venv/bin/activate
    ```

3. Install dependencies using Poetry:
    ```sh
    $ poetry install --sync --all-extras
    ```

4. Setup the required environment variables using the provided `.env.sample` file:
    ```sh
    $ cp .env.sample .env

    # open in your favorite text editor
    $ nano .env
    ```

5. Voila! You're all set to run the bot:
    ```sh
    $ neenee run
    ```

<br>

## 📝 To-do List

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
        - [x] Add basic moderation commands (`/kick`, `/ban`, `/unban`, etc.)
        - [ ] Add advanced moderation commands (`/mute`, `/unmute`, `/warn`, etc.)
    - [ ] Implement a `general` cog for normal commands
- [x] Add advanced features (for now):
    - [x] Improve the logging system and centralize it for universal access
- [ ] Chore tasks:
    - [ ] Add interactive prompts / commands to CLI for easy setup
    - [ ] Add containerization
        - [ ] Add Docker as a build system for the bot
        - [ ] Introduce Docker Compose
        - [ ] Add GitHub Actions to automatically build bot contents on release, and store on ghcr.io