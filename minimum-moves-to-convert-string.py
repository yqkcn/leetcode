class Solution:
    def minimumMoves(self, s: str) -> int:
        res = idx = 0
        while idx < len(s):
            if s[idx] == "O":
                idx += 1
            else:
                res += 1
                idx += 3
        return res