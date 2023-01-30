# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # a, b = 1, 3
        # 1,2,3,4,5,6
        left, right = list1, list1.next
        for i in range(a-1):
            left = left.next
            right = right.next
        for i in range(a, b+1):
            right = right.next
        left.next = list2
        while True:
            if list2.next:
                list2 = list2.next
            else:
                list2.next = right
                break
        return list1
