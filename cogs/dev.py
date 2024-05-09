# SPDX-License-Identifier: MIT


# Imports.
from decouple import config
from disnake import CommandInter, File
from disnake.ext import commands
from disnake.ext.commands import Param

from neenee import Neenee

# Required environment variables.
DISCORD_OWNER_ID = config("DISCORD_OWNER_ID", cast=int)
DEFAULT_GUILD_ID = config("DEFAULT_GUILD_ID", cast=int)


# The Dev cog.
class Dev(commands.Cog):
    def __init__(self, bot: Neenee) -> None:
        self.bot = bot
        bot.add_logger(logger_name="disnake", file_name="disnake.log")

    @commands.slash_command(
        name="reload",
        description="Reload a cog.",
        dm_permission=False,
        guild_ids=[DEFAULT_GUILD_ID],
    )
    @commands.check(lambda inter: inter.author.id == DISCORD_OWNER_ID)
    async def reload(
        self,
        inter: CommandInter,
        name: str = Param(description="The name of the cog."),
    ) -> None:
        try:
            self.bot.reload_extension(name)
        except Exception as e:
            await inter.send(f"Failed to reload cog: `{e}`")
        else:
            await inter.send("Cog reloaded.")

    @commands.slash_command(
        name="getlog",
        description="Get log files for a given logger.",
        dm_permission=False,
        guild_ids=[DEFAULT_GUILD_ID],
    )
    @commands.check(lambda inter: inter.author.id == DISCORD_OWNER_ID)
    async def getlog(
        self,
        inter: CommandInter,
        logger_name: str = Param(description="The name of the logger.", default="neenee"),
    ) -> None:
        try:
            fp = f"logs/{logger_name}.log"
            await inter.send(
                content="Here are your log files!",
                file=File(fp=fp, filename=f"{logger_name}.log"),
                ephemeral=True,
            )
        except Exception as e:
            await inter.send(f"Failed to get log: `{e}`")


# Load the cog.
def setup(bot: Neenee) -> None:
    bot.add_cog(Dev(bot))
