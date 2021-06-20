from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        m, n = len(grid1), len(grid1[0])
        visited = {}
        for i in range(m):
            for j in range(n):
                if not grid1[i][j] or not grid2[i][j]:
                    continue
                if visited.get((i, j)):
                    continue
                members = [(i, j)]
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop()
                    if visited.get((x, y)):
                        continue
                    visited[(x, y)] = True
                    if 0 <= x < m and 0 <= y < n:
                        if not grid2[x][y]:
                            continue
                        members.append((x, y))
                        visited[(x, y)] = True
                        queue.extend([(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)])
                is_ok = True
                for x, y in members:
                    if not grid1[x][y]:
                        is_ok = False
                        break
                if is_ok:
                    res += 1
        return res


if __name__ == '__main__':
    Solution().countSubIslands([[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                               [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]])
