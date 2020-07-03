# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return head
        _set = set()
        while head:
            if head in _set:
                return head
            _set.add(head)
            head = head.next
