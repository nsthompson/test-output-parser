import re
# from pprint import pprint


class ResultParser():

    def __init__(self, suite_list, test_list, keyword_list):
        self.suite_list = suite_list
        self.test_list = test_list
        self.keyword_list = keyword_list

    def parse_results(self):
        # Build Results Dictionary
        results = {
            "suite": {}
        }

        # Parse Suites
        for suite in self.suite_list:
            suite_result = {
                "status": suite['status'],
                "tests": []
            }
            results['suite'][suite['name']] = suite_result

        # pprint("-#### Suites-------------------------------------------")
        # pprint(results)
        # pprint("-------------------------------------------------------")

        # Parse Tests
        for test in self.test_list:
            test_result = {
                "name": test['name'],
                "id": test['id'],
                "status": test['status'],
                "keywords": []
            }
            results['suite'][test['suite']]['tests'].append(test_result)

        # pprint("-#### Tests-------------------------------------------")
        # pprint(results)
        # pprint("-------------------------------------------------------")

        # Parse Keywords
        for keyword in self.keyword_list:
            # Split the originating test id from keyword['id']
            regex_result = re.search(r"^(.*?)-k", keyword['id'])
            test_id = regex_result.group(1)

            # Capture Failure Messages
            for content in keyword['body']:
                failure_message = content.message
                # if content.level in ["ERROR", "FAIL"]:
                #     failure_message = content.message
                # else:
                #     failure_message = None

            keyword_result = {
                "testid": test_id,
                "library": keyword['library'],
                "status": keyword['status'],
                "parent": keyword['parent'].name,
                "message": failure_message
            }

            # Find testid in results dictionary
            for suite in results['suite']:
                for test in results['suite'][suite]['tests']:
                    if test_id == test['id']:
                        test['keywords'].append(keyword_result)

        # pprint("-#### Keywords-------------------------------------------")
        # pprint(results)
        # pprint("-------------------------------------------------------")

        return results
