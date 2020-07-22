package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteNode(head *ListNode, val int) *ListNode {
	pre := &ListNode{}
	pre.Next = head
	for node := pre; node != nil && node.Next != nil; node = node.Next {
		if node.Next.Val == val {
			node.Next = node.Next.Next
			break
		}
	}
	return pre.Next
}
