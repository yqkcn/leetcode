from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                # 对角线
                if i == j or i + j == n -1:
                    if not grid[i][j]:
                        return False
                    continue
                # 得是 0
                if grid[i][j]:
                    return False
        return True
