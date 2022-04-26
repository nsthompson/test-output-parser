from robot.api import ResultVisitor


class SuiteResults(ResultVisitor):

    def __init__(self, suite_list):
        self.suite_list = suite_list

    def start_suite(self, suite):
        if suite.tests:
            stats = suite.statistics

            suite_results = {
                "name": suite.name,
                "id": suite.id,
                "status": suite.status,
                "total": stats.total,
                "pass": stats.passed,
                "fail": stats.failed,
                "skipped": stats.skipped,
                "time": suite.elapsedtime
            }

            self.suite_list.append(suite_results)
