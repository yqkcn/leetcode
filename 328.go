package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	pre1, pre2 := &ListNode{}, &ListNode{}
	pre1.Next, pre2.Next = head, head.Next
	first, second := head, head.Next
	for {
		if second == nil || second.Next == nil {
			// 到最后了
			first.Next = pre2.Next
			break
		}

		first.Next = second.Next
		second.Next = second.Next.Next
		first, second = first.Next, second.Next
	}
	return pre1.Next
}
