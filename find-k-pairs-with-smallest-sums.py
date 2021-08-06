from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        answer = []
        for n1 in nums1[:k]:
            for n2 in nums2[:k]:
                answer.append([n1, n2])
        answer.sort(key=lambda x: x[0] + x[1])
        return answer[:k]
