from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(a, b):
            if grid[a][b] != 1:
                return
            grid[a][b] = "$"
            # 访问邻居
            for r, c in [(a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)]:
                if 0 <= r < m and 0 <= c < n:
                    dfs(r, c)

        # 渲染
        for i in range(m):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][n - 1] == 1:
                dfs(i, n - 1)
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[m - 1][j] == 1:
                dfs(m - 1, j)

        # 计数
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
        print(res)
        return res


if __name__ == '__main__':
    Solution().numEnclaves(
        [
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
    )
