from robot.api import ResultVisitor


class KeywordResults(ResultVisitor):

    def __init__(self, keyword_list, ignore_library, ignore_type):
        self.keyword_list = keyword_list
        self.ignore_library = ignore_library
        self.ignore_type = ignore_type

    def start_keyword(self, keyword):
        if (
            (keyword.libname not in self.ignore_library) and
                (keyword.type not in self.ignore_type)
                ):
            keyword_results = {
                "name": keyword.name,
                "id": keyword.id,
                "status": keyword.status,
                "body": keyword.body,
                "time": keyword.elapsedtime,
                "library": keyword.libname,
                "type": keyword.type,
                "parent": keyword.parent
            }

            self.keyword_list.append(keyword_results)
