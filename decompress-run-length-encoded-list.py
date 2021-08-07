from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums), 2):
            answer.extend([nums[i + 1]] * nums[i])
        return answer
