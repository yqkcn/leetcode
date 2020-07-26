package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func countPairs(root *TreeNode, distance int) int {
	if root == nil {
		return 0
	}
	if root.Left == nil && root.Right == nil {
		return 0
	}
	res := 0
	left := getValues(root.Left, 1)
	right := getValues(root.Right, 1)
	for _, l := range left {
		for _, r := range right {
			if l+r <= distance {
				res += 1
			}
		}
	}
	res += countPairs(root.Left, distance)
	res += countPairs(root.Right, distance)
	return res
}

func getValues(root *TreeNode, depth int) []int {
	if root == nil {
		return []int{}
	}
	if root.Left == nil && root.Right == nil {
		// 叶子节点
		return []int{depth}
	}
	var res []int
	if root.Left != nil {
		res = append(res, getValues(root.Left, depth+1)...)
	}
	if root.Right != nil {
		res = append(res, getValues(root.Right, depth+1)...)
	}
	return res
}
