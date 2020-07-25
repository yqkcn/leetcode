package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}
	var values []int
	for head != nil {
		values = append(values, head.Val)
		head = head.Next
	}
	l, r := 0, len(values) - 1
	for l < r {
		if values[l] != values[r] {
			return false
		}
		l++
		r--
	}
	return true
}
