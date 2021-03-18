# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None:
            return head
        if left == right:
            return head
        pre = ListNode(next=head)
        start1 = start2 = None
        num = 1
        n1, n2 = pre, head
        while True:
            if num < left:
                n1, n2 = n2, n2.next
            elif num == left:
                start1, start2 = n1, n2
                n1, n2 = n2, n2.next
            elif left < num < right:
                cur = n2.next
                n2.next = n1
                n1, n2 = n2, cur
            elif num == right:
                cur = n2.next
                n2.next = n1
                start1.next = n2
                start2.next = cur
                return pre.next
            num += 1
