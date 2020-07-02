# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cache = {}
        while True:
            left = self.get_nums(root.left, cache)
            if left == k - 1:
                return root.val
            if left < k - 1:
                root = root.right
                k = k - left - 1
                continue
            root = root.left

    def get_nums(self, root: TreeNode, cache):
        if not root:
            return 0
        if root.val in cache:
            return cache[root.val]
        cache[root.val] = 1 + self.get_nums(root.left, cache) + self.get_nums(root.right, cache)
        return cache[root.val]
