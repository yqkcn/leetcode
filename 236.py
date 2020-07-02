# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        m, n = p.val, q.val
        cache = {}
        while True:
            if m == root.val or n == root.val:
                return root
            left = self.is_contains(root.left, m, n, cache)
            right = self.is_contains(root.right, m, n, cache)
            if left and right:
                return root
            if left:
                root = root.left
                continue
            root = root.right

    def is_contains(self, node: TreeNode, m, n, cache):
        if not node:
            return False
        if node.val in cache:
            return cache[node.val]
        if node.val == m or node.val == n:
            cache[node.val] = True
            return True
        cache[node.val] = self.is_contains(node.left, m, n, cache) or self.is_contains(node.right, m, n, cache)
        return cache[node.val]
