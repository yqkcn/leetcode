# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        idx = 1
        while idx < len(preorder):
            if preorder[idx] < root.val:
                idx += 1
                continue
            break
        if left := preorder[1:idx]:
            root.left = self.bstFromPreorder(left)
        if right := preorder[idx:]:
            root.right = self.bstFromPreorder(right)
        return root
