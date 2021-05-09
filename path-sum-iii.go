package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, targetSum int) int {
	res := 0
	cache := make(map[*TreeNode]bool)
	var dfs func(*TreeNode, int)
	dfs = func(node *TreeNode, n int) {
		if node == nil {
			return
		}
		if _, ok := cache[node]; !ok {
			cache[node] = true
			dfs(node, targetSum)
		}
		n -= node.Val
		if n == 0 {
			res++
		}
		dfs(node.Left, n)
		dfs(node.Right, n)
	}
	cache[root] = true
	dfs(root, targetSum)
	return res
}