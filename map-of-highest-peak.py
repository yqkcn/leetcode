from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        queue = set()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.add((i, j))
        # 队列
        cache = set()
        ans = 0
        res = [[0] * n for i in range(m)]
        while len(cache) != m * n:
            next_queue = set()
            for a, b in queue:
                if (a, b) in cache:
                    continue
                res[a][b] = ans
                cache.add((a, b))
                # 找邻居
                for i, j in [[a - 1, b], [a, b - 1], [a, b + 1], [a + 1, b]]:
                    if 0 <= i < m and 0 <= j < n and (i, j) not in cache and res[i][j] == 0:
                        next_queue.add((i, j))
            queue = next_queue
            if not queue:
                break
            ans += 1
        return res


if __name__ == '__main__':
    print(Solution().highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
