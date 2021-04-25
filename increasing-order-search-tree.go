package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func increasingBST(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	nodes := BST(root)
	for i, node := range nodes[:len(nodes)-1] {
		node.Right = nodes[i+1]
	}
	return nodes[0]
}

func BST(root *TreeNode) []*TreeNode {
	var res []*TreeNode
	if root == nil {
		return res
	}
	res = append(res, BST(root.Left)...)
	res = append(res, root)
	res = append(res, BST(root.Right)...)
	root.Left = nil
	root.Right = nil
	return res
}
