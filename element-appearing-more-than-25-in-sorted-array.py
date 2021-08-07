from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        import collections
        counter = collections.Counter(arr)
        for k, v in counter.items():
            if v > len(arr) / 4:
                return k
