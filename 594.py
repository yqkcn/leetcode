from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        import collections
        res = 0
        counter = collections.Counter(nums)
        for k in sorted(counter.keys()):
            if k - 1 in counter:
                res = max(res, counter[k] + counter[k - 1])
        return res
