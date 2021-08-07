from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [f"{x:02b}".count("1") for x in range(n + 1)]
