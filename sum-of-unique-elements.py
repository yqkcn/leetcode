from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        import collections
        counter = collections.Counter(nums)
        answer = 0
        for k, v in counter.items():
            if v == 1:
                answer += k
        return answer
