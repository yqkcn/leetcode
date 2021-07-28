from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = num = 0
        for i in gain:
            num += i
            ans = max(ans, num)
        return ans
