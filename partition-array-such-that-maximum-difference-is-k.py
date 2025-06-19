from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = 1
        c = nums[0]
        for num in nums:
            if num - c > k:
                n += 1
                c = num
        return n
