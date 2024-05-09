# SPDX-License-Identifier: MIT


# Imports.
import disnake
from disnake import CommandInter
from disnake.ext import commands
from disnake.ext.commands import Param

from neenee import Neenee


# The Moderation cog.
class Moderation(commands.Cog):
    def __init__(self, bot: Neenee) -> None:
        self.bot = bot
        bot.add_logger(logger_name="disnake", file_name="disnake.log")

    @commands.slash_command(
        name="kick",
        description="Kick a member.",
        dm_permission=False,
    )
    @commands.check(lambda inter: inter.author.guild_permissions.kick_members)
    async def kick(
        self,
        inter: CommandInter,
        member: disnake.Member = Param(description="The member to kick."),
        reason: str = Param(description="The reason for kicking the member."),
    ) -> None:
        try:
            await member.kick(reason=reason)
        except Exception as e:
            await inter.send(f"Failed to kick member: `{e}`")
        else:
            await inter.send(f"Kicked {member}.")

    @commands.slash_command(
        name="ban",
        description="Ban a member.",
        dm_permission=False,
    )
    @commands.check(lambda inter: inter.author.guild_permissions.ban_members)
    async def ban(
        self,
        inter: CommandInter,
        member: disnake.Member = Param(description="The member to ban."),
        reason: str = Param(description="The reason for banning the member."),
    ) -> None:
        try:
            await member.ban(reason=reason)
        except Exception as e:
            await inter.send(f"Failed to ban member: `{e}`")
        else:
            await inter.send(f"Banned {member}.")

    @commands.slash_command(
        name="unban",
        description="Unban a member.",
        dm_permission=False,
    )
    @commands.check(lambda inter: inter.author.guild_permissions.ban_members)
    async def unban(
        self,
        inter: CommandInter,
        member: disnake.User = Param(description="The member to unban."),
        reason: str = Param(description="The reason for unbanning the member."),
    ) -> None:
        try:
            await inter.guild.unban(member, reason=reason)
        except Exception as e:
            await inter.send(f"Failed to unban member: `{e}`")
        else:
            await inter.send(f"Unbanned {member}.")


# Load the cog.
def setup(bot: Neenee) -> None:
    bot.add_cog(Moderation(bot))
