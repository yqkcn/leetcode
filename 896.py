from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        up = None
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                continue
            elif A[i] > A[i-1]:
                if up is None:
                    up = True
                    continue
                elif not up:
                    return False
            elif A[i] < A[i-1]:
                if up is None:
                    up = False
                    continue
                elif up:
                    return False
        return True