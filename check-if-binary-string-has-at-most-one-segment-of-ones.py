class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if "0" not in s:
            return True
        idx = s.index("0")
        return "1" not in s[idx + 1:]
