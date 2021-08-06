from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idx = [i for i, x in enumerate(s) if x == c]
        return [min(abs(i - j) for j in idx) for i, _ in enumerate(s)]
