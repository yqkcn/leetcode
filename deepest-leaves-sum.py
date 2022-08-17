# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        cur = [root]
        deepest = []
        while cur:
            deepest = cur
            next = []
            for node in cur:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if next:
                cur = next
                deepest = next
            else:
                break
        return sum(node.val for node in deepest)