from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(n):
            cur = []
            for j in range(m):
                cur.append(matrix[j][i])
            res.append(cur)
        return res