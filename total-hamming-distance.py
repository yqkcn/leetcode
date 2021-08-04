from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        length = len(nums)
        answer = 0
        for i in range(30):
            # 统计第 i 位上 1 的个数
            a = sum((x >> i & 1) for x in nums)
            answer += a * (length - a)
        return answer
