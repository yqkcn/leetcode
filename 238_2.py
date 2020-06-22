from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        cur = 1
        for i in range(len(nums) - 1):
            cur *= nums[i]
            res[i + 1] = cur
        cur = 1
        for i in range(len(nums) - 1, 0, -1):
            cur *= nums[i]
            res[i - 1] *= cur
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
