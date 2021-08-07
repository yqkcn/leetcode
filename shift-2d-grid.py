from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        data = []
        for x in grid:
            data.extend(x)
        k %= len(data)
        data = data[-k:] + data[: -k]
        for i in range(m):
            for j in range(n):
                grid[i][j] = data.pop(0)

        return grid
