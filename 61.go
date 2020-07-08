package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}
	var nums []int
	var nodes []*ListNode
	for node := head; ; {
		if node == nil {
			break
		}
		nums = append(nums, node.Val)
		nodes = append(nodes, node)
		node = node.Next
	}
	if k%len(nodes) == 0 {
		return head
	}
	path := k % len(nodes)
	for i := 0; i < len(nodes); i++ {
		if i >= path {
			nodes[i].Val = nums[i - path]
		} else {
			nodes[i].Val = nums[len(nodes) - path + i]
		}
	}
	return head
}
