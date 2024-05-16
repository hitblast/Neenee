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

---

> [!IMPORTANT]
> Neenee is currently in development and not yet recommended for production use, however you can take part in shaping it's future by [submitting an issue](https://github.com/hitblast/Neenee/issues) to let us know what you think.

---

<br>

## 🔖 Table of Contents

- [Overview](#-overview)
- [Setup](#-setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [To-do List](#-to-do-list)
- [Contributing](#-contributing)
    - [Code of Conduct](./CODE_OF_CONDUCT.md)

<br>

## ✨ Overview

Neenee is a next-generation, highly scalable Discord bot aimed at moderators, developers (and people who generally love bots!) to help them manage their server, perform moderation tasks (while listening to music) and just have fun in general while using Discord.

### 🚀 Features

- **Scalable** - Neenee is built with a fully modular architecture that allows you to add or remove parts as needed.
- **Robust** - The project relies on Python 3.12, the latest production version of the language.
- **Intuitive** - Neenee can be easily configured, unlike other bots, which rely on boring configuration guides.
- **Creative** - Ever feel like most bots on the platform have the same features? Neenee is here to change that. With every update, we aim to bring new and exciting features to the table.
- **Open-source** - Yeah, we absolutely <3 open source! Does that even need an explanation? :D

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

<br>

## 🤝 Contributing

New ideas, feature requests and bug reports are always welcome! Have a look at our [GitHub Issues](https://github.com/hitblast/Neenee/issues) for any open or unresolved issues.

If you are a developer who is looking forward to contributing to Neenee, please refer to the [Code of Conduct](./CODE_OF_CONDUCT.md) before contributing.

<br>

---

<div align="center">

### 🌟 Feel free to star the repository if you like it! :D 

</div>
