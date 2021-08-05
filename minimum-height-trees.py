from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        import collections

        if n == 1:
            return [0]

        paths = collections.defaultdict(set)
        degree = collections.defaultdict(int)
        for edge in edges:
            paths[edge[0]].add(edge[1])
            paths[edge[1]].add(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        # 出度为1的是叶子节点
        queue = []
        for k, v in degree.items():
            if v == 1:
                queue.append(k)

        res = []  # 存储结果
        while queue:
            res = queue[::-1]
            next_queue = []
            for num in queue:
                for n in paths[num]:
                    degree[n] -= 1
                    if degree[n] == 1:
                        next_queue.append(n)
            queue = next_queue
        return res
