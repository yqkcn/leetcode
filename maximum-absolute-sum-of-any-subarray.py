from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_num = max_num = sum_num = 0
        result = abs(nums[0])
        for num in nums:
            print(min_num, max_num, sum_num)
            sum_num += num
            result = max(result, abs(sum_num - min_num), abs(sum_num - max_num))
            min_num, max_num = min(min_num, sum_num), max(max_num, sum_num)
        return result


if __name__ == '__main__':
    Solution().maxAbsoluteSum([-3, -5, -3, -2, -6, 3, 10, -10, -8, -3, 0, 10, 3, -5, 8, 7, -9, -9, 5, -8])
