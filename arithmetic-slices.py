from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                count += 1
            else:
                result += count * (count + 1) // 2
                count = 0
        return result + count * (count + 1) // 2
