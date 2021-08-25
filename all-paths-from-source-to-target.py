from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        _map = {i: v for i, v in enumerate(graph)}
        visited = []
        res = []

        def dfs():
            if visited[-1] == n - 1:
                res.append(list(visited))
                return
                # 枚举所有情况
            for num in _map[visited[-1]]:
                visited.append(num)
                dfs()
                visited.pop()

        visited.append(0)
        dfs()
        return res


if __name__ == '__main__':
    Solution().allPathsSourceTarget([[1,2],[3],[3],[]])