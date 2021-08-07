from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        import collections
        r_counter = collections.defaultdict(int)
        c_counter = collections.defaultdict(int)
        for r, c in indices:
            r_counter[r] += 1
            c_counter[c] += 1
        answer = 0
        for i in range(m):
            for j in range(n):
                if (r_counter[i] + c_counter[j]) % 2:
                    answer += 1
        return answer
