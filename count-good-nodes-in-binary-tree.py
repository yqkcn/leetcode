# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def find(node, max_num):
            nonlocal res
            if not node:
                return
            if node.val >= max_num:
                res += 1
            find(node.left, max(node.val, max_num))
            find(node.right, max(node.val, max_num))

        res = 0
        if root:
            find(root, root.val)
        return res
