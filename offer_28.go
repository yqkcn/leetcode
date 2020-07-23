package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	queue := [][2]*TreeNode{{root.Left, root.Right}}
	for len(queue) != 0 {
		node1 := queue[len(queue)-1][0]
		node2 := queue[len(queue)-1][1]
		queue = queue[:len(queue)-1]
		if node1 == nil && node2 == nil {
			continue
		} else if node1 == nil || node2 == nil {
			return false
		} else if node1.Val != node2.Val {
			return false
		} else {
			queue = append(queue, [2]*TreeNode{node1.Left, node2.Right})
			queue = append(queue, [2]*TreeNode{node1.Right, node2.Left})
		}
	}
	return true
}
