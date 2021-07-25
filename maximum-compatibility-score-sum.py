from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        num = 0

        def dfs(i, cur, _set: set):
            nonlocal num
            if i == m:
                return

            for j in _set:
                _n = 0
                for k in range(n):
                    if students[i][k] == mentors[j][k]:
                        _n += 1
                _set.remove(j)
                num = max(num, _n + cur)
                dfs(i + 1, cur + _n, _set)
                _set.add(j)

        dfs(0, 0, set(range(m)))
        return num
