package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeDuplicateNodes(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	cache := make(map[int]bool)
	pre := &ListNode{}
	pre.Next = head
	first, second := pre, head
	for second != nil {
		if cache[second.Val] {
			second = second.Next
			continue
		}
		first.Next = second
		cache[second.Val] = true
		first, second = second, second.Next
		first.Next = nil
	}
	return pre.Next
}
