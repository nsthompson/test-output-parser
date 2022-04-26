from .robot import robot_markdown_output


def markdown_output(framework, results):
    if framework == "robot":
        # Generate Markdown output for Robot Formatted Data
        tables = robot_markdown_output(results)

    # Output Tables
    for table in tables:
        print(f'\n{table}')
