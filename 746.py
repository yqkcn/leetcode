from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a = b = 0
        for i in range(2, n + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b
