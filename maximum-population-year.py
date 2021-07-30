from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        import collections
        birth, dieth = collections.defaultdict(int), collections.defaultdict(int)
        for a, b in logs:
            birth[a] += 1
            dieth[b] += 1
        answer = 0
        num = 0
        res = 0
        for i in range(1949, 2051):
            print(answer)
            num += birth[i]
            num -= dieth[i]
            if num > answer:
                answer = num
                res = i
            answer = max(answer, num)
        return res


if __name__ == '__main__':
    Solution().maximumPopulation([[1993, 1999], [2000, 2010]])
