import collections
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = collections.Counter(answers)
        res = 0
        for k, v in counter.items():
            if k == 0:
                res += v
            elif v <= k + 1:
                res += k + 1
            else:
                num = v // (k + 1)
                if v % (k + 1):
                    num += 1
                res += num * (k + 1)
        return res


if __name__ == '__main__':
    print(Solution().numRabbits([0, 1, 0, 2, 0, 1, 0, 2, 1, 1]))
