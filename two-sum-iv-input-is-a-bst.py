# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def _get_value(node):
            if node is None:
                return []
            return _get_value(node.left) + [node.val] + _get_value(node.right)

        values = _get_value(root)
        for i in range(len(values) - 1):
            for j in range(i + 1, len(values)):
                if values[i] + values[j] == k:
                    return True
        return False
