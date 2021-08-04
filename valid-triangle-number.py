from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                left, right = j + 1, n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        left = mid + 1
                    else:
                        right = mid - 1
                answer += left - 1 - j
        return answer


if __name__ == '__main__':
    print(Solution().triangleNumber([2, 2, 3, 4]))
