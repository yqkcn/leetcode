import itertools
from typing import List
import math
import functools


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        cache = {}
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                cache[(i, j)] = math.gcd(nums[i], nums[j])
        items = set()  # 忽略组内顺序，去重
        def dfs(num, cur):
            if num == len(nums):


        for item in itertools.permutations(range(len(nums)), len(nums)):
            cur = []
            for i in range(0, len(item), 2):
                cur.extend(sorted(item[i: i+2]))
            items.add(tuple(cur))
        res = 0
        for item in items:
            cur = 0
            for i in range(1, len(nums) // 2 + 1):
                a, b, *item = item
                cur += i * cache[(a, b)]
            res = max(res, cur)
        return res


if __name__ == '__main__':
    Solution().maxScore([773274,313112,131789,222437,918065,49745,321270,74163,900218,80160,325440,961730])
