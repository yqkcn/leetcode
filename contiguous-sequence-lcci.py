class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        min_num = nums[0]
        total = nums[0]
        res = nums[0]
        for num in nums[1:]:
            total += num
            res = max(res, total - min_num, total)
            min_num = min(min_num, total)
        return res