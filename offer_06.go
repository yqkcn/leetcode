package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reversePrint(head *ListNode) []int {
	if head == nil {
		return []int{}
	}
	var cur []int
	for node := head; node != nil; node = node.Next {
		cur = append(cur, node.Val)
	}
	var res []int
	for i := len(cur) - 1; i >= 0; i-- {
		res = append(res, cur[i])
	}
	return res
}
