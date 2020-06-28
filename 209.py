# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            if cur >= s:
                return 1
            for j in range(i + 1, len(nums)):
                if res and j - i + 1 > res:
                    break
                cur += nums[j]
                if cur >= s:
                    res = min(res, j - i + 1) if res else j - i + 1
                    break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 2, 1]))
    print(s.minSubArrayLen(11, [1, 2, 3, 4, 5, 18]))
