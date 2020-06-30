# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, nodes = [], [root]
        left_first = True
        while nodes:
            values, next_nodes = [], []
            for node in nodes:
                values.append(node.val)
                if left_first:
                    if node.left:
                        next_nodes.insert(0, node.left)
                    if node.right:
                        next_nodes.insert(0, node.right)
                else:
                    if node.right:
                        next_nodes.insert(0, node.right)
                    if node.left:
                        next_nodes.insert(0, node.left)
            res.append(values)
            nodes = next_nodes
            left_first = not left_first
        return res
