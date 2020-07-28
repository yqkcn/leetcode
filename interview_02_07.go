package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	cache := make(map[*ListNode]bool)
	for headA != nil {
		cache[headA] = true
		headA = headA.Next
	}
	for headB != nil {
		if cache[headB] {
			return headB
		} else {
			headB = headB.Next
		}
	}
	return nil
}
