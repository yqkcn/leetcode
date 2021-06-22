from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i in range(len(timeSeries)):
            if i == 0:
                res += duration
                continue
            delta = timeSeries[i] - timeSeries[i - 1]
            if delta < duration:
                res += delta
            else:
                res += duration
        return res
