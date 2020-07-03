from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_num = float("-inf")
        pres = [1]
        for num in nums:
            cur = []
            for pre in pres:
                _num = num * pre
                cur.append(_num)
                max_num = max(max_num, _num)
            pres = [1, max(cur), min(cur)]
        return max_num


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))
    print(s.maxProduct([-2, 0, -1]))
