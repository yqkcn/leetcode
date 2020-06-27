from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1
        while True:
            if res not in nums:
                return res
            res += 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([3, 4, -1, 1]))
