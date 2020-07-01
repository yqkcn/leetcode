from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        res = 0
        dq = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(m - 1, - 1, -1):
            for j in range(n - 1, -1, -1):
                if A[i] == B[j]:
                    dq[i][j] = dq[i + 1][j + 1] + 1
                    res = max(res, dq[i][j])
        return res
