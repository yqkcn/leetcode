package main


// Definition for a binary tree node.
type TreeNode struct {
     Val int
     Left *TreeNode
     Right *TreeNode
 }

func hasPathSum(root *TreeNode, sum int) bool {
	if root == nil {
		return false
	}
	type NodeSum struct {
		Node *TreeNode
		Sum int
	}

	nodes := []NodeSum{{root, 0}}
	for len(nodes) != 0 {
		node := nodes[len(nodes) - 1]
		nodes = nodes[:len(nodes) - 1]
		if node.Node.Val + node.Sum == sum && node.Node.Left == nil && node.Node.Right == nil {
			return true
		}
		if node.Node.Left != nil {
			nodes = append(nodes, NodeSum{node.Node.Left, node.Sum + node.Node.Val})
		}
		if node.Node.Right != nil {
			nodes = append(nodes, NodeSum{node.Node.Right, node.Sum + node.Node.Val})
		}
	}
	return false
}


if not root:
return False
nodes = [(0, root)]
while nodes:
parent_num, node = nodes.pop()
if not node:
continue
if (cur_num := node.val + parent_num) == sum and not node.left and not node.right:
return True
if node.left:
nodes.append((cur_num, node.left))
if node.right:
nodes.append((cur_num, node.right))
return False