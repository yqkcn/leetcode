from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        left, right = 0, 1
        result = 0
        delta = nums[right] - nums[left]
        while True:
            # 结束
            print(left, right, result)
            if right == len(nums) - 1:
                if nums[right] - nums[right - 1] == delta:
                    num = right - left + 1
                else:
                    num = right - left
                result += (num - 2) * (num - 1) // 2
                break
            # 仍是等差数列，添加
            if nums[right] - nums[right - 1] == delta:
                right += 1
                continue
            # 不是等差数列，计算当前子数组包含的个数
            num = right - left
            result += (num - 2) * (num - 1) // 2
            left = right - 1
            delta = nums[right] - nums[left]
        return result

if __name__ == '__main__':
    Solution().numberOfArithmeticSlices([1,2,3,4,4,14,4,252,52,525,25,4,5,3,5,3,4,4,4,3,3])