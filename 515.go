package main

import "sort"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func largestValues(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var res []int
	queue := []*TreeNode{root}
	for len(queue) != 0 {
		var nextQueue []*TreeNode
		var cur []int
		for _, node := range queue {
			cur = append(cur, node.Val)
			if node.Left != nil {
				nextQueue = append(nextQueue, node.Left)
			}
			if node.Right != nil {
				nextQueue = append(nextQueue, node.Right)
			}
		}
		sort.Ints(cur)
		res = append(res, cur[len(cur)-1])
		queue = nextQueue
	}
	return res
}
