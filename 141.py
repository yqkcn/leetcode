# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        _set = set()
        node = head
        while node:
            if node in _set:
                return True
            _set.add(node)
            node = node.next
        return False
