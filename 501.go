package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findMode(root *TreeNode) []int {
	values := getValues(root)
	count := make(map[int]int)
	for _, num := range values {
		count[num]++
	}
	maxNum := 0
	for _, v := range count {
		if v > maxNum {
			maxNum = v
		}
	}
	var res []int
	for k, v := range count {
		if v == maxNum {
			res = append(res, k)
		}
	}
	return res
}

func getValues(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	res := []int{root.Val}
	res = append(res, getValues(root.Left)...)
	res = append(res, getValues(root.Right)...)
	return res
}
