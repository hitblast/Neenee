# Imports.
from decouple import config
from disnake import CommandInter
from disnake.ext import commands
from disnake.ext.commands import Param

from neenee import Neenee

# Required environment variables.
DISCORD_OWNER_ID = config('DISCORD_OWNER_ID', cast=int)


# The Dev cog.
class Dev(commands.Cog):
    def __init__(self, bot: Neenee) -> None:
        self.bot = bot
        bot._add_logger(logger_name='disnake', file_name='debug.log')

    @commands.slash_command(name='ping', description='Pong!', dm_permission=False)
    async def ping(self, inter: CommandInter) -> None:
        await inter.send(f'Pong! ({self.bot.latency * 1000:.0f}ms)')

    @commands.slash_command(
        name='reload',
        description='Reload a cog.',
        dm_permission=False,
    )
    @commands.check(lambda inter: inter.author.id == DISCORD_OWNER_ID)
    async def reload(
        self,
        inter: CommandInter,
        name: str = Param(description='The name of the cog.'),
    ) -> None:
        try:
            self.bot.reload_extension(name)
        except Exception as e:
            await inter.send(f'Failed to reload cog: `{e}`')
        else:
            await inter.send('Cog reloaded.')


# Load the cog.
def setup(bot: Neenee) -> None:
    bot.add_cog(Dev(bot))