from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import collections
        paths = collections.defaultdict(list)
        for s, e, c in times:
            paths[s].append((e, c))

        visited = set()
        queue = [(0, k)]
        total_time = 0
        while queue:
            queue.sort(key=lambda x: x[0])
            i, j = queue.pop(0)
            visited.add(j)
            total_time = max(i, total_time)
            for e, c in paths[j]:
                if e in visited:
                    continue
                queue.append((i + c, e))
            queue = [x for x in queue if x[1] not in visited]
        if len(visited) != n:
            return -1
        return total_time


if __name__ == '__main__':
    print(Solution().networkDelayTime(times=[[1,2,1],[2,3,2],[1,3,4]], n=3, k=1))
