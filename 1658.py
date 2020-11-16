from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if x == total:
            return len(nums)
        target = total - x
        left, right = 0, 0
        length = len(nums)
        cur = 0
        res = -1
        while left < length and right < length:
            if cur + nums[right] == target:
                if right - left + 1 > res:
                    res = right - left + 1
                cur -= nums[left]
                left += 1
            elif cur + nums[right] < target:
                cur += nums[right]
                right += 1
            elif cur + nums[right] > target:
                cur -= nums[left]
                left += 1
        return length - res if res != -1 else -1


if __name__ == '__main__':
    print(Solution().minOperations([3,2,20,1,1,3], 10))
