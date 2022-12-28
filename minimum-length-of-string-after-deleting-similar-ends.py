class Solution:
    def minimumLength(self, s: str) -> int:
        while True:
            if len(s) <= 1 or s[0] != s[-1]:
                break
            s = s.strip(s[0])
        return len(s)