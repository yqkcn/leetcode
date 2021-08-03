from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        answer = 0
        cur = 0
        total = 0
        while satisfaction:
            item = satisfaction.pop()
            cur += item
            total += cur
            answer = max(answer, total)
        return answer


if __name__ == '__main__':
    print(Solution().maxSatisfaction([-1,-8,0,5,-7]))