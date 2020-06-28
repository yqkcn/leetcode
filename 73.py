from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in range(len(matrix)):
            if i in row:
                matrix[i] = [0] * len(matrix[0])
                continue
            for j in range(len(matrix[0])):
                if j in col:
                    matrix[i][j] = 0



if __name__ == '__main__':
    s = Solution()
    s.setZeroes([
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ])
