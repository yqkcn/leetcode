from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            return len([x for x in items if x[0] == ruleValue])
        if ruleKey == "color":
            return len([x for x in items if x[1] == ruleValue])
        if ruleKey == "name":
            return len([x for x in items if x[2] == ruleValue])