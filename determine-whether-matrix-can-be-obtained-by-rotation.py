from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        n = len(mat)
        for i in range(3):
            new_mat = []
            for j in range(n):
                new_mat.append([x[j] for x in mat][::-1])
            if new_mat == target:
                return True
            mat = new_mat
        return False
