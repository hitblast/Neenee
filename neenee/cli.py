# SPDX-License-Identifier: MIT


# Imports.
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
console = Console()


# Helper functions for CLI commands.
def _print_err(text: str) -> None:
    console.print(text, style="red")
    return click.echo(err=True)


# The main function for running the bot.
@cli.command("run", help="Run the bot.")
def _run() -> None:
    # Create a new instance of Neenee.
    from neenee import build_core

    neenee = build_core()

    try:
        # Run the bot.
        neenee.run(config("DISCORD_TOKEN", cast=str))
    except Exception as e:
        _print_err(f"error -_- {e}")
