# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ans = []

        def visit(node: TreeNode, vs: list[int]) -> bool:
            if not node:
                return True
            if not vs:
                return False
            if vs[0] != node.val:
                return False
            # 没有子节点
            if not node.left and not node.right:
                return True
            # 只有一个子节点
            if not node.left or not node.right:
                return visit(node.left or node.right, vs[1:])
            # 两个子节点
            if len(vs) < 3:
                return False
            # 不需要旋转
            if node.left.val == vs[1]:
                if node.right.val not in vs:
                    return False
                idx = vs.index(node.right.val)
                return visit(node.left, vs[1:idx]) and visit(node.right, vs[idx:])
            # 需要旋转
            if node.right.val == vs[1]:
                if node.left.val not in vs:
                    return False
                ans.append(node.val)
                idx = vs.index(node.left.val)
                return visit(node.left, vs[idx:]) and visit(node.right, vs[1:idx])
            return False

        if not visit(root, voyage):
            return [-1]
        return ans
