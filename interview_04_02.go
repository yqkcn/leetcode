package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	if len(nums) == 1 {
		return &TreeNode{Val: nums[0]}
	}
	idx := len(nums) / 2
	root := &TreeNode{Val: nums[idx]}
	if idx > 0 {
		root.Left = sortedArrayToBST(nums[:idx])
	}
	if idx < len(nums)-1 {
		root.Right = sortedArrayToBST(nums[idx+1:])
	}
	return root
}
