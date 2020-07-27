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
	left, right := 0, len(values)-1
	for left < right {
		if values[left] != values[right] {
			return false
		}
		left++
		right--
	}
	return true
}
