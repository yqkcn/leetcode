from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        answer = float("inf")
        for i, num in enumerate(nums):
            if num == target:
                if abs(i - start) < answer:
                    answer = abs(i - start)
        return answer
