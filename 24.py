class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(self, head: ListNode) -> ListNode:
    if not head.next:
        return head
    _temp = ListNode(None)
    _temp.next = head.next
    first, second = head, head.next
    pre, end = None, None
    while first and second:
        end = second.next or end
        second.next = first
        first.next = end
        if pre:
            pre.next = second
        pre = first
        first, second = first.next, first.next.next if first.next else None
    return _temp.next
