# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.sort(key=lambda x: x.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]