class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        num = 0
        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) == 3:
                num += 1
        return num
