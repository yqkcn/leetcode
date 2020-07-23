package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getKthFromEnd(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	num := 1
	for node := head; node != nil; node = node.Next {
		num += 1
	}
	node := &ListNode{}
	node.Next = head
	for curNum := 1; node.Next != nil && curNum < num-k+1; curNum++ {
		node = node.Next
	}
	return node
}
