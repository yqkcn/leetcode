# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, _sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        nodes = [([], root)]
        while nodes:
            parent_num, node = nodes.pop()
            if node.val + sum(parent_num) == _sum and not node.left and not node.right:
                res.append(parent_num + [node.val])
                continue
            if node.left:
                nodes.append((parent_num + [node.val], node.left))
            if node.right:
                nodes.append((parent_num + [node.val], node.right))
        return res
