from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max1 = [max(x[i] for x in grid) for i in range(n)]
        max2 = [max(x) for x in grid]
        res = 0
        for i in range(m):
            for j in range(n):
                res += min(max2[i], max1[j]) - grid[i][j]
        return res
