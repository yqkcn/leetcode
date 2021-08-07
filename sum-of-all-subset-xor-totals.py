from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subs = [[]]
        for num in nums:
            new_subs = []
            for sub in subs:
                new_subs.append(sub + [num])
            subs.extend(new_subs)
        answer = 0
        for sub in subs:
            cur = 0
            for num in sub:
                cur ^= num
            answer += cur
        return answer
