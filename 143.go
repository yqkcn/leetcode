package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode) {
	if head == nil {
		return
	}
	var nodes []*ListNode
	node := head
	for ; node != nil; {
		nodes = append(nodes, node)
		node = node.Next
	}
	if len(nodes) == 1 {
		return
	}
	pre := &ListNode{Val: 0, Next: head}
	for i, j := 0, len(nodes)-1; i <= j; {
		nodes[i].Next = nil
		nodes[j].Next = nil
		if i == j {
			pre.Next = nodes[i]
			break
		}
		pre.Next = nodes[i]
		nodes[i].Next = nodes[j]
		pre = nodes[j]
		i++
		j--
	}
}
