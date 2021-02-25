# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        max_num = max(nums)
        for i, num in enumerate(nums):
            if num == max_num:
                node = TreeNode(max_num)
                if i > 0:
                    node.left = self.constructMaximumBinaryTree(nums[:i])
                if i < len(nums) - 1:
                    node.right = self.constructMaximumBinaryTree(nums[i+1:])
                return node