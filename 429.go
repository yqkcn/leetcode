package main

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func levelOrder(root *Node) [][]int {
	if root == nil {
		return [][]int{}
	}
	var res [][]int
	queue := []*Node{root}
	for len(queue) != 0 {
		var nextQueue []*Node
		var cur []int
		for _, node := range queue {
			cur = append(cur, node.Val)
			nextQueue = append(nextQueue, node.Children...)
		}
		res = append(res, cur)
		queue = nextQueue
	}
	return res
}
