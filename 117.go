package main

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	if root.Left == nil && root.Right == nil {
		return root
	}
	//寻找root右侧节点的最左边一个子节点
	var nextRightChild *Node
	for next := root.Next; next != nil; next = next.Next {
		if next.Left != nil {
			nextRightChild = next.Left
			break
		}
		if next.Right != nil {
			nextRightChild = next.Right
			break
		}
	}
	if root.Right != nil {
		root.Right.Next = nextRightChild
		connect(root.Right)
		nextRightChild = root.Right
	}
	if root.Left != nil {
		root.Left.Next = nextRightChild
		connect(root.Left)
	}
	return root
}
