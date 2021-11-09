package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isEvenOddTree(root *TreeNode) bool {
	level := 0
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		var nextQueue []*TreeNode
		if level == 0 {
			pre := 0
			for _, node := range queue {
				if node.Val <= pre || node.Val%2 == 0 {
					return false
				} else {
					pre = node.Val
					if node.Left != nil {
						nextQueue = append(nextQueue, node.Left)
					}
					if node.Right != nil {
						nextQueue = append(nextQueue, node.Right)
					}
				}
			}
			level = 1
		} else {
			pre := math.MaxInt64
			for _, node := range queue {
				if node.Val >= pre || node.Val%2 != 0 {
					return false
				} else {
					pre = node.Val
					if node.Left != nil {
						nextQueue = append(nextQueue, node.Left)
					}
					if node.Right != nil {
						nextQueue = append(nextQueue, node.Right)
					}
				}
			}
			level = 0
		}
		queue = nextQueue
	}
	return true
}
