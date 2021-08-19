from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        length = len(nums)
        mid = length // 2
        nums1 = nums[:mid]
        nums2 = nums[mid:][::-1]
        _len = min(len(nums1), len(nums2))
        answer = []
        for i in range(_len):
            answer.append(nums2[i])
            answer.append(nums1[i])
        if _len < len(nums1):
            answer.append(nums1[-1])
        elif _len < len(nums2):
            answer.append(nums2[-1])
        return answer
