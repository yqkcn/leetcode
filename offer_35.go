package main

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */
var cache = make(map[*Node]*Node)

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}
	if node, ok := cache[head]; ok {
		return node
	}
	newNode := &Node{Val: head.Val}
	cache[head] = newNode
	newNode.Next = copyRandomList(head.Next)
	newNode.Random = copyRandomList(head.Random)
	return newNode
}
