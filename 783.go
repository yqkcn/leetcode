package main

import (
	"math"
	"sort"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDiffInBST(root *TreeNode) int {
	values := getValues(root)
	sort.Ints(values)
	res := math.MaxInt64
	for i := 0; i < len(values)-1; i++ {
		if values[i+1]-values[i] < res {
			res = values[i+1] - values[i]
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
