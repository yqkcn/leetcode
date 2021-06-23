from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -1000000
        cur = sum(nums[:k])
        idx = k
        length = len(nums)
        while True:
            if cur / k > res:
                res = cur / k
            if idx >= length:
                break
            cur += nums[idx]
            cur -= nums[idx - k]
            idx += 1
        return res


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)

        return maxTotal / k