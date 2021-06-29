from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        import collections

        counter = collections.defaultdict(list)
        for path in paths:
            names = path.split(" ")
            directory = names[0]
            for file in names[1:]:
                name, content = file.split("(")
                name = f"{directory}/{name}"
                content = content[:-1]
                counter[content].append(name)
        return [v for k, v in counter.items() if len(v) > 1]
