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
console = Console(record=True)


# Helper functions for CLI commands.
def print_err(text: str) -> None:
    console.print(text, style="red")
    return click.echo(err=True)


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

    try:
        # Run the bot.
        neenee = build_core(force_dev=dev)

        token = token or config("DISCORD_TOKEN", cast=str)
        neenee.run(token)

    except Exception as e:
        print_err(f"error -_- \n\n{'\n  '.join(getattr(e, 'message', str(e)).split(':'))}")
