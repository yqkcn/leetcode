from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        side = max(min(x) for x in rectangles)
        return len([1 for x in rectangles if x[0] >= side and x[1] >= side])
