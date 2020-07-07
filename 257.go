package main

import "strconv"

func binaryTreePaths(root *TreeNode) []string {
	var res []string
	if root == nil {
		return res
	}
	return getPath(root)
}

func getPath(root *TreeNode) []string {
	var res []string
	if root == nil {
		return res
	}
	if root.Left == nil && root.Right == nil {
		res = append(res, strconv.Itoa(root.Val))
		return res
	}
	res = append(res, getPath(root.Left)...)
	res = append(res, getPath(root.Right)...)
	var newRes []string
	for _, path := range res {
		newRes = append(newRes, strconv.Itoa(root.Val) + "->" + path)
	}
	return newRes
}