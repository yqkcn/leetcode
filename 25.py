class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        _temp = ListNode(None)
        _temp.next = head
        pre, curr = _temp, head

        while curr:
            currs = []
            for i in range(k):
                if not curr:
                    break
                currs.append(curr)
                curr = curr.next
            if len(currs) < k:
                break
            if pre:
                pre.next = currs[-1]
            pre = currs[0]
            for i in range(k - 1):
                currs[i + 1].next = currs[i]

        return _temp.next
