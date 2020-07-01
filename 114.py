# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        all_nodes = []
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if not node:
                continue
            all_nodes.append(node)
            nodes.append(node.right)
            nodes.append(node.left)
        for i in range(len(all_nodes) - 1):
            all_nodes[i].right = all_nodes[i + 1]
            all_nodes[i].left = None
        all_nodes[-1].right = None
        all_nodes[-1].left = None
