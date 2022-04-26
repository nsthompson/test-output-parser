import rich_click as click

from core.config import config
from lib.parsers.robot import RobotParser
from lib.output import cli_output, markdown_output


# Collect filename at runtime
@click.command()
@click.option(
    '--framework',
    'framework',
    required=True,
    type=click.Choice(['robot'], case_sensitive=False),
    help=(
        'Test Framework: '
        '[robot] for Robot framework'
    )
)
@click.option(
    '--file',
    'filename',
    required=True,
    type=click.Path(exists=True, readable=True),
    help='Path to test output file'
)
@click.option(
    '--output',
    'output_choice',
    required=True,
    type=click.Choice(['cli', 'markdown'], case_sensitive=False),
    help=(
        'Output Method: '
        '[cli] for rich command-line output '
        '[markdown] for markdown formatted tables'
    )
)
def parse_output(framework, filename, output_choice):
    # Load Parser based on framework
    if framework == "robot":
        parser = RobotParser(config, filename)
        results = parser.parse_robot()

    # Route Output based on output_choice
    if output_choice == "cli":
        cli_output(framework, results)
    elif output_choice == "markdown":
        markdown_output(framework, results)


if __name__ == "__main__":
    parse_output()  # pylint: disable=no-value-for-parameter
