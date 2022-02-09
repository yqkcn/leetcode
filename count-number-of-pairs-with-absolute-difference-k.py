from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        num = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    num += 1
        return num
