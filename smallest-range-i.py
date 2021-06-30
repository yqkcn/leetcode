from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_num = max(nums) - k
        min_num = min(nums) + k
        return 0 if min_num >= max_num else max_num - min_num
