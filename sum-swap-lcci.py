from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1, sum2 = sum(array1), sum(array2)
        if sum1 == sum2:
            return []
        delta = abs(sum1 - sum2)
        if delta % 2:
            return []
        nums1, nums2 = sorted(set(array1)), sorted(set(array2))
        target = delta // 2
        if sum1 > sum2:
            target *= -1
        for num in nums1:
            if num + target in nums2:
                return [num, num + target]
        return []