from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                answer += k - j
        return answer


if __name__ == '__main__':
    print(Solution().triangleNumber([2, 2, 3, 4]))
