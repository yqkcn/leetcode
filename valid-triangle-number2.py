from typing import List
import bisect


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        num = 0
        for i, num1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                idx = bisect.bisect_left(nums[j+1:], num1 + num2)
                if idx != 0:
                    num += idx
        return num


if __name__ == '__main__':
    cases = [
        [4, 2, 3, 4]
    ]
    for case in cases:
        a = Solution().triangleNumber(case)
        print(a)