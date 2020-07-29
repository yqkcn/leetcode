package main

import (
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func recoverFromPreorder(S string) *TreeNode {
	return inner(S, "-")
}

func inner(S string, prefix string) *TreeNode {
	// 找到根节点
	var cur string
	for i := 0; i < len(S); i++ {
		if S[i] == '-' {
			break
		} else {
			cur += string(S[i])
		}
	}
	num, _ := strconv.Atoi(cur)
	root := &TreeNode{Val: num}
	left := len(cur) + len(prefix)
	for i := left; i < len(S); i++ {
		if strings.HasPrefix(S[i:], prefix) && !strings.HasPrefix(S[i:], prefix+"-") && S[i-1] != '-' {
			// 到右节点
			root.Left = inner(S[left:i], prefix+"-")
			root.Right = inner(S[i+len(prefix):], prefix+"-")
			break
		} else if i == len(S)-1 {
			root.Left = inner(S[left:], prefix+"-")
		}
	}
	return root
}
