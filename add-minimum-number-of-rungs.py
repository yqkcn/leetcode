from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        if not rungs:
            return 0
        rungs.insert(0, 0)
        res = 0
        for i in range(1, len(rungs)):
            delta = rungs[i] - rungs[i - 1]
            if delta <= dist:
                continue
            a, b = delta // dist, delta % dist
            a = a if b else a - 1
            res += a
        return res
