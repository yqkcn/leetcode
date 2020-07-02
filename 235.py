# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        m, n = p.val, q.val
        if m > n:
            m, n = n, m
        while True:
            if m <= root.val and n >= root.val:
                return root
            if n < root.val:
                root = root.left
                continue
            if m > root.val:
                root = root.right
