import collections
from typing import List

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counter, counter_counter = collections.defaultdict(int), collections.defaultdict(int)
        res = 2
        for i, num in enumerate(nums):
            # 第一次碰到
            if num not in counter:
                counter[num] += 1
                # 统计数量
                counter_counter[1] += 1
            # 不是第一次
            else:
                n = counter[num]
                counter[num] += 1
                counter_counter[n] -= 1
                if counter_counter[n] == 0:
                    counter_counter.pop(n)
                counter_counter[n+1] += 1
            if len(counter_counter) == 1:
                key = list(counter_counter.keys())[0]
                if key == 1 or counter_counter[key] == 1:
                    res = max(res, i + 1)
            # 包含两个元素
            elif len(counter_counter) == 2:
                # 其中一个 key = 1
                if 1 in counter_counter and counter_counter[1] == 1:
                    res = max(res, i + 1)
                    continue
                key1, key2 = list(counter_counter.keys())
                # key1 = key2 + 1 且 val1 = 1
                if key1 - key2 == 1 and counter_counter[key1] == 1:
                    res = max(res, i + 1)
                    continue
                # key2 = key1 + 1 且 val2 = 1
                if key2 - key1 == 1 and counter_counter[key2] == 1:
                    res = max(res, i + 1)
                    continue
        return res