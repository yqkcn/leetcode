# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        nodes = [(0, root)]
        while nodes:
            parent_num, node = nodes.pop()
            if not node:
                continue
            if (cur_num := node.val + parent_num) == sum and not node.left and not node.right:
                return True
            if node.left:
                nodes.append((cur_num, node.left))
            if node.right:
                nodes.append((cur_num, node.right))
        return False
