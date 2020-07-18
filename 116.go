package main

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func connect(root *Node) *Node {
	if root == nil || root.Left == nil {
		return root
	}
	markNode(root)
	return root
}

func markNode(node *Node) {
	node.Left.Next = node.Right
	if node.Next != nil {
		node.Right.Next = node.Next.Left
	}
	connect(node.Left)
	connect(node.Right)
}
