import pandas as pd


def robot_markdown_output(results):
    # Empty List for Return Results
    tables = []

    # Build Suite Results Dataframe
    suites = []
    status = []

    for suite in results['suite']:
        suites.append(suite)
        status.append(results['suite'][suite]['status'])

    # Build List of Tuples for Dataframe
    result_tuple = list(zip(suites, status))

    # Generate Dataframe from result_tuple
    suite_df = pd.DataFrame(result_tuple, columns=['Suite', 'Status'])
    suite_md = suite_df.to_markdown(index=False)
    tables.append(suite_md)

    # Build Detailed Results Dataframe
    suites = []
    tests = []
    library = []
    status = []
    parents = []
    messages = []

    for suite in results['suite']:
        for test in results['suite'][suite]['tests']:
            for keyword in test['keywords']:
                suites.append(suite)
                tests.append(test['name'])
                library.append(keyword['library'])
                status.append(keyword['status'])
                parents.append(keyword['parent'])
                messages.append(keyword['message'])

    details = zip(*[suites, tests, library, status, parents, messages])

    details_columns = [
        "Suite",
        "Test Name",
        "Library",
        "Status",
        "Parent",
        "Message"
        ]

    details_df = pd.DataFrame(details, columns=details_columns)
    details_md = details_df.to_markdown(index=False)
    tables.append(details_md)

    return tables
