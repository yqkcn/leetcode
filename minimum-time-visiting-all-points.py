from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        if len(points) == 1:
            return answer
        for i in range(1, len(points)):
            a, b = points[i]
            c, d = points[i - 1]
            answer += max(abs(b - d), abs(a - c))
        return answer
