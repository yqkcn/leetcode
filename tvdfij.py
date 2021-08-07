from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            print(left)
            if left * 2 + nums[i] == total:
                return i
            left += nums[i]
        return -1


if __name__ == '__main__':
    Solution().pivotIndex([-1, -1, -1, -1, -1, 0])
