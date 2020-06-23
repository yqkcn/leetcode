from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        return [_ + extraCandies >= _max for _ in candies]
