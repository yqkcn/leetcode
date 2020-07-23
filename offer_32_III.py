class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, nodes = [], [root]
        leftFirst = True
        while nodes:
            values, next_nodes = [], []
            for node in nodes:
                values.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if leftFirst:
                res.append(values)
            else:
                res.append(values[::-1])
            nodes = next_nodes
            leftFirst = not leftFirst
        return res
