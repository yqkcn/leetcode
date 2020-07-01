# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        nodes = [root]
        while nodes:
            next_nodes = []
            for node in nodes:
                if not node.left and not node.right:
                    return res
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes
            res += 1
        return res
