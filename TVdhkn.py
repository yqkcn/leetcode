from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for num in nums:
            new_list = []
            for x in answer:
                new_list.append(x + [num])
            answer.extend(new_list)
        return answer
