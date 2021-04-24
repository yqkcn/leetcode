package main


Definition for a Node.
type Node struct {
	Val       int
	Neighbors []*Node
}

func cloneGraph(node *Node) *Node {
	visited := map[*Node]*Node{}
	var cp func(*Node) *Node
	cp = func(node *Node) *Node {
		if node == nil {
			return node
		}
		if n, ok := visited[node]; ok {
			return n
		}
		cloneNode := &Node{Val: node.Val, Neighbors: []*Node{}}
		visited[node] = cloneNode
		for _, nei := range node.Neighbors {
			cloneNode.Neighbors = append(cloneNode.Neighbors, cp(nei))
		}
		return cloneNode
	}
	return cp(node)
}
