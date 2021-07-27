from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dq = [0] + [float("inf")] * time
        for i in range(1, time + 1):
            for a, b in clips:
                if a < i <= b:
                    dq[i] = min(dq[i], dq[a] + 1)
        return -1 if dq[time] == float("inf") else dq[time]
