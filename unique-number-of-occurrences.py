from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        import collections

        counter = collections.Counter(arr)
        return len(counter) == len(set(counter.values()))
