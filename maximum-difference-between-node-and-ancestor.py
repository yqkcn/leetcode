# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node: TreeNode, min_num: int, max_num: int):
            nonlocal ans

            ans = max(ans, abs(node.val - min_num), abs(max_num - node.val))
            if node.val < min_num:
                min_num = node.val
            elif node.val > max_num:
                max_num = node.val
            if node.left:
                dfs(node.left, min_num, max_num)
            if node.right:
                dfs(node.right, min_num, max_num)

        dfs(root, root.val, root.val)
        return ans
