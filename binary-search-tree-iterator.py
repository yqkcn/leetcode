# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        def _middle(node):
            if node is None:
                return []
            return _middle(node.left) + [node.val] + _middle(node.right)

        self.values = _middle(root)

    def next(self) -> int:
        return self.values.pop(0)

    def hasNext(self) -> bool:
        return bool(self.values)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
