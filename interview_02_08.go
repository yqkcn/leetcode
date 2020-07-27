package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
	cache := make(map[*ListNode]bool)
	for head != nil {
		if cache[head] {
			return head
		}
		cache[head] = true
		head = head.Next
	}
	return head
}
