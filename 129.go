package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumNumbers(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	for _, num := range getPaths(root, 0) {
		res += num
	}
	return res
}

func getPaths(root *TreeNode, pre int) []int {
	var res []int
	// 终止到叶子节点,不能传入空接点
	if root.Left == nil && root.Right == nil {
		res = append(res, pre+root.Val)
		return res
	}
	// 找左节点和右节点
	if root.Left != nil {
		res = append(res, getPaths(root.Left, (pre+root.Val)*10)...)
	}
	if root.Right != nil {
		res = append(res, getPaths(root.Right, (pre+root.Val)*10)...)
	}
	return res
}
