from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = None
        # 判断所有组合
        m, n = len(nums1), len(nums2)
        for i in range(max(k - n, 0), min(m, k) + 1):
            sequence1 = self.get_max_sequence(nums1, i)
            sequence2 = self.get_max_sequence(nums2, k - i)
            print(len(sequence1), len(sequence2), k)
            sequence = self.merge_sequence(sequence1, sequence2)
            if not res or self.compare(sequence, res):
                res = sequence
        return res

    def get_max_sequence(self, nums, k):
        """取出k个元素组成最大值"""
        stack = []
        target = len(nums) - k  # 删除个数

        for num in nums:
            while stack and target and num > stack[-1]:
                stack.pop()
                target -= 1
            stack.append(num)
        if target > 0:
            stack = stack[:-target]
        return stack

    def merge_sequence(self, num1, num2):
        """合并为最大序列"""
        res = []
        idx1 = idx2 = 0
        while idx1 < len(num1) and idx2 < len(num2):
            if self.compare(num1[idx1:], num2[idx2:]):
                res.append(num1[idx1])
                idx1 += 1
            else:
                res.append(num2[idx2])
                idx2 += 1
        # 未添加完的
        res.extend(num1[idx1:])
        res.extend(num2[idx2:])
        return res

    def compare(self, num1, num2) -> bool:
        idx1 = idx2 = 0
        while idx1 < len(num1) and idx2 < len(num2):
            if num1[idx1] > num2[idx2]:
                return True
            elif num1[idx1] < num2[idx2]:
                return False
            else:
                idx1 += 1
                idx2 += 1
        return len(num1) > len(num2)


if __name__ == '__main__':
    Solution().maxNumber([6, 7], [6, 0, 4], 5)
