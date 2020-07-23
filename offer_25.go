package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}
	pre := &ListNode{}
	start := pre
	node1 := l1
	node2 := l2
	for node1 != nil && node2 != nil {
		if node1.Val < node2.Val {
			pre.Next, pre, node1 = node1, node1, node1.Next
		} else {
			pre.Next, pre, node2 = node2, node2, node2.Next
		}
	}
	if node1 != nil {
		pre.Next = node1
	} else if node2 != nil {
		pre.Next = node2
	}
	return start.Next
}
