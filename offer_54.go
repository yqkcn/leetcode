package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthLargest(root *TreeNode, k int) int {
	values := in(root)
	return values[len(values)-k]
}

func in(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var res []int
	res = append(res, in(root.Left)...)
	res = append(res, root.Val)
	res = append(res, in(root.Right)...)
	return res
}
