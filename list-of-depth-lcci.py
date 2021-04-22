# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        res = []
        if not tree:
            return []
        queue = [tree]
        while queue:
            next_queue = []
            head = ListNode(None)
            node = head
            for q in queue:
                if q.left:
                    next_queue.append(q.left)
                if q.right:
                    next_queue.append(q.right)
                node.next = ListNode(q.val)
                node = node.next
            res.append(head.next)
            queue = next_queue
        return res
