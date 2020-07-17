package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	values := make(map[int]int)
	node := head
	for node != nil {
		values[node.Val]++
		node = node.Next
	}
	pres := &ListNode{}
	start := pres
	node = head
	for node != nil {
		if values[node.Val] == 1 {
			pres.Next = node
			tmp := node.Next
			node.Next = nil
			pres = node
			node = tmp
			continue
		}
		node = node.Next
	}
	return start.Next
}
