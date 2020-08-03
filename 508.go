package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findFrequentTreeSum(root *TreeNode) []int {
	cache := make(map[*TreeNode]int)
	count := make(map[int]int)
	getSum(root, cache)
	for _, v := range cache {
		count[v]++
	}
	max := 0
	for _, v := range count {
		if v > max {
			max = v
		}
	}
	var res []int
	for k, v := range count {
		if v == max {
			res = append(res, k)
		}
	}
	return res
}

func getSum(node *TreeNode, cache map[*TreeNode]int) int {
	if node == nil {
		return 0
	}
	if num, ok := cache[node]; ok {
		return num
	}
	cache[node] = node.Val + getSum(node.Left, cache) + getSum(node.Right, cache)
	return cache[node]
}
