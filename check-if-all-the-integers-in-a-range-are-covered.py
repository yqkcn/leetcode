from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            ok = False
            for start, end in ranges:
                if start <= num <= end:
                    ok = True
                    break
            if not ok:
                return False
        return True
