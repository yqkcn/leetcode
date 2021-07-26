from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        return heapq.nsmallest(k, points, key=lambda x: x[0] ** 2 + x[1] ** 2)
