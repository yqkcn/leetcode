package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func kthToLast(head *ListNode, k int) int {
	// 计数
	num := 0
	for node := head; node != nil; node = node.Next {
		num++
	}
	idx := 1
	for node := head; node != nil; node = node.Next {
		if idx == num-k+1 {
			return node.Val
		} else {
			idx++
		}
	}
	return 666
}
