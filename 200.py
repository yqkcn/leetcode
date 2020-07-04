from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        marked = set()
        num = 0
        for i in range(m):
            for j in range(n):
                if (i, j) in marked:
                    continue
                if grid[i][j] == "0":
                    marked.add((i, j))
                    continue
                num += 1
                labors = [(i, j)]
                while labors:
                    r, c = labors.pop()
                    if 0 <= r < m and 0 <= c < n:
                        if (r, c) in marked:
                            continue
                        marked.add((r, c))
                        if grid[r][c] == "1":
                            labors.extend([(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)])
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    ))
    print(s.numIslands([
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    ))
