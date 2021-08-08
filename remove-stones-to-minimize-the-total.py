import collections
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        counter = collections.Counter(piles)
        while k:
            key = max(counter.keys())
            v = counter[key]
            if v <= k:
                k -= v
                counter.pop(key)
                counter[key - key // 2] += v
            else:
                counter[key] = v - k
                counter[key - key // 2] += k
                k = 0
        print(counter)
        return sum(i * j for i, j in counter.items())


if __name__ == '__main__':
    print(Solution().minStoneSum([5, 4, 9], 2))
