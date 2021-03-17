from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        import collections
        counter = collections.Counter(nums)
        double = miss = None
        l = len(nums)
        for i in range(1, l + 1):
            if not counter.get(i):
                miss = i
            elif counter.get(i) == 2:
                double = i
            if double is not None and miss is not None:
                return [double, miss]
