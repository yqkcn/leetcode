from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        answer = -1
        distance = float("inf")
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                cur = abs(a - x) + abs(b - y)
                if cur < distance:
                    distance = cur
                    answer = i
        return answer
