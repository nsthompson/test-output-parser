from robot.api import ResultVisitor


class TestResults(ResultVisitor):

    def __init__(self, test_list):
        self.test_list = test_list

    def visit_test(self, test):
        test_results = {
            "suite": str(test.parent),
            "name": test.name,
            "id": test.id,
            "status": test.status,
            "time": test.elapsedtime,
            "starttime": test.starttime,
            "endtime": test.endtime,
            "tags": test.tags
        }

        self.test_list.append(test_results)
