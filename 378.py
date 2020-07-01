from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for _ in matrix:
            res.extend(_)
        return res[k - 1]