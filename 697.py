from collections import Counter
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        counter = Counter(nums)
        max_num = max(counter.values())
        if max_num == 1:
            return 1
        values = [k for k, v in counter.items() if v == max_num]
        min_len = len(nums)
        for value in values:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] == value and nums[r] == value:
                    min_len = min(min_len, r - l + 1)
                    break
                elif nums[l] == value:
                    r -= 1
                elif nums[r] == value:
                    l += 1
                else:
                    l += 1
                    r -= 1
        return min_len
