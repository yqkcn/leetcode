from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def _sort_func(x, y):
            return int(x + y) - int(y + x)

        nums = [str(num) for num in nums]
        nums = sorted(nums, key=cmp_to_key(_sort_func), reverse=True)
        print(nums)
        return str(int("".join(nums)))


if __name__ == '__main__':
    Solution().largestNumber([3, 30, 34, 5, 9])
