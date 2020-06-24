from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        _max = _cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                _cur += 1
                continue
            _max = max(_max, _cur)
            _cur = 1
        return max(_max, _cur)


if __name__ == '__main__':
    s = Solution()
    # print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
    # print(s.longestConsecutive([0, -1]))
    # print(s.longestConsecutive([1, 0, -1]))
    print(s.longestConsecutive([1, 2, 0, 1]))
