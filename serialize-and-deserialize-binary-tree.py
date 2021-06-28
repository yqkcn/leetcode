# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(data: list):
            val = data.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs(data)
            node.right = dfs(data)
            return node
        data = data.split(",")
        return dfs(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))