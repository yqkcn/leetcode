package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isUnivalTree(root *TreeNode) bool {
	if root == nil {
		return true
	}
	target := root.Val
	var check func(node *TreeNode) bool
	check = func(node *TreeNode) bool {
		if node == nil {
			return true
		}
		return node.Val == target && check(node.Left) && check(node.Right)
	}
	return check(root)
}
