package main

import "math"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findTilt(root *TreeNode) int {
	ans := 0
	var sumTree func(node *TreeNode) int
	sumTree = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := sumTree(node.Left)
		right := sumTree(node.Right)
		ans += int(math.Abs(float64(left - right)))
		return left + right + node.Val
	}
	sumTree(root)
	return ans
}
