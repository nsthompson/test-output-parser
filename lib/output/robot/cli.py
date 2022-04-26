from rich import box
from rich.table import Table


def robot_cli_output(results):
    # Empty List of Tables
    tables = []

    # Generate Results Table for Suites
    suite_table = Table(
        title="Test Suite Results",
        show_header=True,
        header_style="bold blue",
        box=box.ROUNDED,
        show_lines=True
    )
    suite_table.add_column("Suite")
    suite_table.add_column("Status")
    for suite in results['suite']:
        if results['suite'][suite]['status'] == "PASS":
            status = (
                f"[bold green]"
                f"{results['suite'][suite]['status']}"
                f"[/bold green]"
            )
        elif results['suite'][suite]['status'] == "FAIL":
            status = (
                f"[bold red]"
                f"{results['suite'][suite]['status']}"
                f"[/bold red]"
            )
        suite_table.add_row(
            suite,
            status
        )

    tables.append(suite_table)

    # Generate Detailed Results Table
    results_table = Table(
        title="Detailed Test Results",
        show_header=True,
        header_style="bold blue",
        box=box.ROUNDED,
        show_lines=True
    )
    results_table.add_column("Suite")
    results_table.add_column("Test Name")
    results_table.add_column("Library")
    results_table.add_column("Status")
    results_table.add_column("Parent")
    results_table.add_column("Message")
    for suite in results['suite']:
        for test in results['suite'][suite]['tests']:
            for keyword in test['keywords']:
                if keyword['status'] == "PASS":
                    status = f"[bold green]{keyword['status']}[/bold green]"
                elif keyword['status'] == "FAIL":
                    status = f"[bold red]{keyword['status']}[/bold red]"
                results_table.add_row(
                    suite,
                    test['name'],
                    keyword['library'],
                    status,
                    keyword['parent'],
                    keyword['message']
                )
    tables.append(results_table)

    return tables
