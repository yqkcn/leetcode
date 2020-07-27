package main

import "strconv"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var s1 string
	var s2 string
	for l1 != nil {
		s1 = strconv.Itoa(l1.Val) + s1
		l1 = l1.Next
	}
	for l2 != nil {
		s2 = strconv.Itoa(l2.Val) + s2
		l2 = l2.Next
	}
	num1, _ := strconv.Atoi(s1)
	num2, _ := strconv.Atoi(s2)
	num := num1 + num2
	head := &ListNode{}
	pre := head
	for num != 0 {
		if num < 10 {
			head.Val = num
			break
		}
		head.Val = num % 10
		num = num / 10
		head.Next = &ListNode{}
		head = head.Next
	}
	return pre
}
