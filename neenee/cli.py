# SPDX-License-Identifier: MIT


# Imports.
import traceback

import click
from decouple import config
from rich.console import Console


# Create a new group for putting the CLI commands.
@click.group(
    help="An elegant & scalable Discord bot which aces in robustness (and in doing chores :D)"
)
@click.version_option(
    package_name="Neenee",
    message="Package: %(prog)s, version %(version)s\n",
)
def cli() -> None:
    pass


# Initialize Console object for rich-based output.
console = Console(record=True)


# Create the run command which starts a new instance of Neenee.
@cli.command("run", help="Boots up Neenee.")
@click.option(
    "--token",
    "-t",
    type=str,
    help="The token of the bot. If not passed, it will be fetched from the environment.",
    required=False,
)
@click.option(
    "--dev",
    "-d",
    is_flag=True,
    help="Run Neenee in development mode.",
)
def _run(token: str, dev: bool) -> None:
    # Create a new instance of Neenee.
    from neenee import build_core

    neenee = build_core(force_dev=dev)

    try:
        # Run the bot.
        token = token or config("DISCORD_TOKEN", cast=str)
        neenee.run(token)

    except Exception as e:
        # Print the error message.
        traceback.print_exception(type(e), e, e.__traceback__)
        neenee.log(f"[bold red]\nerror -_-\n\n{e}[/bold red]", level="err")
