package main

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func maxDepth(root *Node) int {
	if root == nil {
		return 0
	}
	if len(root.Children) == 0 {
		return 1
	}
	res := 0
	queue := []*Node{root}
	for len(queue) != 0 {
		var nextQueue []*Node
		for _, node := range queue {
			nextQueue = append(nextQueue, node.Children...)
		}
		res++
		queue = nextQueue
	}
	return res
}
