from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        min_m, max_m = 0, len(matrix) - 1
        min_n, max_n = 0, len(matrix[0]) - 1
        m, n = 0, 0
        target = len(matrix) * len(matrix[0])
        res = []
        while len(res) != target:
            if m == min_m:
                if n == min_n:
                    for i in range(n, max_n + 1):
                        res.append(matrix[m][i])
                    m += 1
                    n = max_n
                    min_m += 1
                else:
                    for i in range(m, max_m + 1):
                        res.append(matrix[i][n])
                    max_n -= 1
                    n -= 1
                    m = max_m
                continue
            if m == max_m:
                if n == min_n:
                    for i in range(m, min_m - 1, -1):
                        res.append(matrix[i][n])
                    n += 1
                    min_n += 1
                    m = min_m
                else:
                    for i in range(n, min_n - 1, -1):
                        res.append(matrix[m][i])
                    max_m -= 1
                    m -= 1
                    n = min_n
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
