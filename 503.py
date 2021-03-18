from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [-1] * length
        stack = []
        for i, num in enumerate(nums + nums):
            if not stack:
                if i < length:
                    stack.append((i, num))
                else:
                    break
            while stack and num > stack[-1][1]:
                item = stack.pop()
                res[item[0]] = num
            # 入栈
            if i < length:
                stack.append((i, num))
        return res


if __name__ == '__main__':
    Solution().nextGreaterElements([1, 2, 1])
