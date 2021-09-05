from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        answer = []
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j] != 0:
                    continue
                # 碰到池塘
                num = 0
                queue = [(i, j)]
                while queue:
                    next_queue = []
                    for a, b in queue:
                        if a <0 or a >= m or b <0 or b >=n:
                            continue
                        if land[a][b] != 0:
                            continue
                        land[a][b] = 1
                        num += 1
                        next_queue.extend([(a-1, b-1), (a-1,b), (a-1, b+1), (a, b-1), (a, b+1), (a+1, b-1), (a+1, b), (a+1, b+1)])
                    queue = next_queue
                answer.append(num)
        return sorted(answer)