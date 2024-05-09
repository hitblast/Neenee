# SPDX-License-Identifier: MIT


# Imports.
from __future__ import annotations

import logging
import os
import traceback
from typing import Any, List, Self

import disnake
from decouple import config
from disnake import CommandInter
from disnake.ext import commands

from .cli import console

# Required evironment variables.
DEV_MODE = config("DEV_MODE", cast=bool, default=False)


# Set up the base bot class.
class Neenee(commands.AutoShardedInteractionBot):
    """
    The core class for Neenee, holding the required components for initializing the bot properly.

    Parameters:
    - initial_extensions (List[str]): A list of initial extensions to load when Neenee starts.
    """

    def __init__(self: Self, *args: Any, initial_extensions: List[str], **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.logger: logging.Logger = self.add_logger(logger_name="neenee", file_name="neenee.log")

        console.clear()
        for extension in initial_extensions:
            self.log(f"Loading extension: [bold yellow]{extension}[/bold yellow]")
            self.load_extension(extension)

    @staticmethod
    def add_logger(*, logger_name: str, file_name: str) -> logging.Logger:
        """
        Adds a logger to the bot.

        Parameters:
        - logger_name (str): The name of the logger.
        - file_name (str): The name of the file to log to.

        Returns:
        - logging.Logger: The logger instance.
        """

        logger = logging.getLogger(logger_name)
        logger.setLevel(disnake.logging.DEBUG)

        if not os.path.exists("logs"):
            os.makedirs("logs")

        handler = logging.FileHandler(filename=f"logs/{file_name}", encoding="utf-8", mode="w")
        handler.setFormatter(
            disnake.logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
        )
        logger.addHandler(handler)

        return logger

    def log(self: Self, message: str) -> None:
        """
        Logs a message to the console.

        Parameters:
        - message (str): The message to log.
        """

        console.print(message)
        plain_message = console.export_text()[:-1]
        self.logger.info(plain_message)

    async def _update_presence(self: Self) -> None:
        """
        Updates the rich presence of the bot.
        """

        await self.change_presence(
            status=disnake.Status.dnd,
            activity=disnake.Activity(
                type=disnake.ActivityType.listening,
                name=f"commands inside {len(self.guilds)} server(s)!",
            ),
        )

    async def on_connect(self: Self) -> None:
        await self._update_presence()
        self.log(f"Connected to Discord as: [bold cyan]{self.user}[/bold cyan]")

    async def on_ready(self: Self) -> None:
        self.log("[bold green]I'm ready! :D[/bold green]")

    async def on_guild_join(self: Self, _: disnake.Guild) -> None:
        await self._update_presence()

    async def on_guild_remove(self: Self, _: disnake.Guild) -> None:
        await self._update_presence()

    async def on_message(self: Self, message: disnake.Message) -> None:
        if message.author == self.user:
            return

    async def on_slash_command_error(self: Self, inter: CommandInter, error: Exception) -> None:
        traceback.print_exception(type(error), error, error.__traceback__)
        await inter.send(f"An error occurred: {error}")


# Basic build_core() function for returning a new instance of Neenee.
# Note: This should be used in the main file, not in this file.
def build_core() -> Neenee:
    initial_extensions = [
        "cogs.moderation",
    ]

    if DEV_MODE:
        initial_extensions.append("cogs.dev")

    instance = Neenee(initial_extensions=initial_extensions)
    instance.log("Operating in [bold red]development mode.[/bold red]\n")
    return instance
