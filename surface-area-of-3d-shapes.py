from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res += grid[i][j] * 4 + 2
                # 去掉重复计算的面积
                for r, c in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c]:
                        res -= min(grid[i][j], grid[r][c])
        return res
