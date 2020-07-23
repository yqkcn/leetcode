class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, nodes = [], [root]
        while nodes:
            values, next_nodes = [], []
            for node in nodes:
                values.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            res.extend(values)
            nodes = next_nodes
        return res
