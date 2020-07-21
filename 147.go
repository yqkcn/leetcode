package main

import "math"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertionSortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	preHead := &ListNode{Val: math.MaxInt64}
	preHead.Next = head
	cur, next := head, head.Next
	for next != nil {
		if next.Val > cur.Val {
			cur = next
			next = next.Next
			continue
		}
		// 断开
		cur.Next = next.Next
		pre1, pre2 := preHead, preHead.Next
		for next.Val > pre2.Val {
			pre1 = pre2
			pre2 = pre2.Next
		}
		pre1.Next = next
		next.Next = pre2
		next = cur.Next
	}
	return preHead.Next
}
