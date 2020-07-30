package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
	sum := 0
	queue := []*TreeNode{root}
	for len(queue) != 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur == nil {
			continue
		}
		if cur.Right != nil {
			queue = append(queue, cur.Right)
		}
		if cur.Left != nil {
			if cur.Left.Left == nil && cur.Left.Right == nil {
				sum += cur.Left.Val
			} else {
				queue = append(queue, cur.Left)
			}
		}
	}
	return sum
}
