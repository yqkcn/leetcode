package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	cache := make(map[int]bool)
	pres := &ListNode{}
	start := pres
	for head != nil {
		if cache[head.Val] {
			head = head.Next
			continue
		}
		pres.Next = head
		pres = head
		cache[head.Val] = true
		tmp := head.Next
		head.Next = nil
		head = tmp
	}
	return start.Next
}

func deleteDuplicates2(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	curr, next := head, head.Next

	for next != nil {
		if curr.Val == next.Val {
			next = next.Next
		} else {
			curr.Next = next
			curr = next
			next = next.Next
		}
	}
	curr.Next = nil
	return head
}
