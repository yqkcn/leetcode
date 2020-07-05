package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeElements(head *ListNode, val int) *ListNode {
	if head == nil {
		return head
	}
	pre := new(ListNode)
	pre.Next = head
	first := pre
	second := head
	for second != nil {
		if second.Val == val {
			first.Next = second.Next
			second = second.Next
		} else {
			first, second = second, second.Next
		}
	}
	return pre.Next
}
