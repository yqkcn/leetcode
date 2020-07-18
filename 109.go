package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedListToBST(head *ListNode) *TreeNode {
	var values []int
	for node := head; node != nil; {
		values = append(values, node.Val)
		node = node.Next
	}
	return getNode(values)
}

func getNode(values []int) *TreeNode {
	if len(values) == 0 {
		return nil
	}
	if len(values) == 1 {
		return &TreeNode{Val: values[0]}
	}
	if len(values) == 2 {
		node := &TreeNode{Val: values[0]}
		node.Right = &TreeNode{Val: values[1]}
		return node
	}
	// 取中点
	node := &TreeNode{Val: values[len(values)/2]}
	node.Left = getNode(values[0 : len(values)/2])
	node.Right = getNode(values[len(values)/2+1:])
	return node
}
