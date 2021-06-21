from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        cur = nums[0]
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                cur += nums[idx]
            else:
                cur = nums[idx]
            if cur > res:
                res = cur
        return res
