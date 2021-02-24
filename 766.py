from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or not matrix[0]:
            return True
        m, n = len(matrix), len(matrix[0])
        nodes = [(0, i) for i in range(n)] + [(j, 0) for j in range(m)]
        for r, c in nodes:
            num = matrix[r][c]
            while r < m and c < n:
                if matrix[r][c] != num:
                    return False
                r += 1
                c += 1
        return True
