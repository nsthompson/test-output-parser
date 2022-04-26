from robot.api import ExecutionResult

from .results import ResultParser
from .suite import SuiteResults
from .tests import TestResults
from .keywords import KeywordResults


class RobotParser():

    def __init__(self, config, filename):
        self.filename = filename
        self.suite_list = []
        self.test_list = []
        self.keyword_list = []

        # Load Libraries and Types to Ignore from config
        self.ignore_library = config.IGNORE_LIBRARIES
        self.ignore_type = config.IGNORE_TYPES

    def parse_robot(self):
        # Load Output File
        result = ExecutionResult(self.filename)
        # Parse Suite Results
        result.visit(SuiteResults(self.suite_list))
        # Parse Test Results
        result.visit(TestResults(self.test_list))

        # Parse Keyword Results
        result.visit(KeywordResults(
            self.keyword_list,
            self.ignore_library,
            self.ignore_type
            )
        )

        # Generate Results Dict
        parser = ResultParser(
            self.suite_list,
            self.test_list,
            self.keyword_list
            )
        results = parser.parse_results()

        return results
