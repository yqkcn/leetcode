from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        idx1 = idx2 = 0
        while idx1 < len(firstList) and idx2 < len(secondList):
            # 无交集
            s1, e1 = firstList[idx1]
            s2, e2 = secondList[idx2]
            if e2 < s1:
                idx2 += 1
            elif s2 <= s1 <= e2 <= e1:
                answer.append([s1, e2])
                idx2 += 1
            elif s2 <= s1 <= e1 <= e2:
                answer.append([s1, e1])
                idx1 += 1
            elif s1 <= s2 <= e2 <= e1:
                answer.append([s2, e2])
                idx2 += 1
            elif s1 <= s2 <= e1 <= e2:
                answer.append([s2, e1])
                idx1 += 1
            elif e1 < s2:
                idx1 += 1

        return answer
