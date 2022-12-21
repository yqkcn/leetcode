from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            y = (left + right) // 2
            ops = sum((x - 1) // y for x in nums)
            if ops <= maxOperations:
                right = y
            else:
                left = y + 1

        return right


if __name__ == '__main__':
    print(Solution().minimumSize([2, 4, 8, 2], 4))
