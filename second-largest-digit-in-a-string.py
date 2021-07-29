class Solution:
    def secondHighest(self, s: str) -> int:
        s = set(int(x) for x in s if x.isdigit())
        s = sorted(s)
        if len(s) < 2:
            return -1
        return s[-2]
