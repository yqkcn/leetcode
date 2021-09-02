class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        left, right = 0, 0
        n = len(nums)
        cur = nums[0]
        while right < n:
            if cur >= target:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
            else:
                right += 1
                if right < n:
                    cur += nums[right]
        return 0 if res == float("inf") else res