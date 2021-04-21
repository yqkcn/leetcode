# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l, r = p.val, q.val
        if l > r:
            l, r = r, l
        return self.find(root, l, r)

    def find(self, node, l, r):
        if node.val < l:
            return self.find(node.right, l, r)
        if node.val > r:
            return self.find(node.left, l, r)
        return node
