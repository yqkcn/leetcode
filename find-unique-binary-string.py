from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums[0])
        nums = set(int(num, 2) for num in nums)
        i = 0
        while True:
            if i not in nums:
                return f"{i:0{l}b}"
            i += 1
