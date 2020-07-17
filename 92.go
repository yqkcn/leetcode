package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, m int, n int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	start1 := &ListNode{}
	start2 := &ListNode{}
	first, second := &ListNode{}, head
	first.Next = second
	pre := first
	for i := 0; ; i++ {
		if i < m-1 {
			first = second
			second = second.Next
			continue
		}
		if i == m-1 {
			start1 = first
			start2 = second
			first = second
			second = second.Next
			continue
		}
		if i < n {
			tmp := second.Next
			second.Next = first
			first = second
			second = tmp
			continue
		}
		if i == n {
			start1.Next = first
			start2.Next = second
			break
		}
	}
	return pre.Next
}
