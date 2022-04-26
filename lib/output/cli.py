from rich.console import Console

from .robot import robot_cli_output


def cli_output(framework, results):
    console = Console()

    if framework == "robot":
        # Generate Tables for Robot Formatted Data
        tables = robot_cli_output(results)

    # Output Tables to CLI
    for table in tables:
        console.print(table)
