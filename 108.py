# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.get_middle_mode(nums)

    def get_middle_mode(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        node = TreeNode(nums[len(nums) // 2])
        node.left = self.get_middle_mode(nums[:len(nums) // 2])
        node.right = self.get_middle_mode(nums[len(nums) // 2 + 1:])
        return node
