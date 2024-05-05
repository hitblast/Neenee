# SPDX-License-Identifier: MIT


# Imports.
from __future__ import annotations

import logging
import os
import traceback
from typing import Any, List, Self

import disnake
from disnake import CommandInter
from disnake.ext import commands

from .cli import console


# Set up the base bot class.
class Neenee(commands.AutoShardedInteractionBot):
    """
    The core class for Neenee, holding the required components for initializing the bot properly.
    """

    def __init__(self: Self, *args: Any, initial_extensions: List[str], **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for extension in initial_extensions:
            self.load_extension(extension)

    def _add_logger(self, *, logger_name: str, file_name: str) -> None:
        """
        Adds a logger to the bot.
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

    async def _update_presence(self: Self) -> None:
        """
        Updates the rich presence of IgKnite.
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
        console.print(f"\nConnected to Discord as: [bold yellow]{self.user}[/bold yellow]")

    async def on_ready(self: Self) -> None:
        console.print("[bold green]I'm ready! :D[/bold green]")

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
    return Neenee(
        initial_extensions=[
            "cogs.dev",
        ],
    )
