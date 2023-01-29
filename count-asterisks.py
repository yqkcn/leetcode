class Solution:
    def countAsterisks(self, s: str) -> int:
        res = num = cur = 0
        for i in s:
            if i == "|":
                num += 1
                if num == 2:
                    cur = num = 0
                elif num == 1:
                    res, cur = res + cur, 0
            elif i == "*":
                cur += 1
        return res + cur
