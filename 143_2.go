package main

import "fmt"

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
	if head.Next == nil {
		return
	}
	slow, fast := head, head
	for {
		if fast.Next == nil {
			break
		}
		if fast.Next.Next == nil {
			slow = slow.Next
			fast = fast.Next
			break
		}
		slow = slow.Next
		fast = fast.Next.Next
	}
	// 断开
	// 有 head，有 last，依次取一个
	last := reverseList(slow.Next)
	fmt.Print(last.Val)
	slow.Next = nil
	first := head
	pre := &(ListNode{})
	for {
		if first == nil && last == nil {
			break
		}
		if first != nil {
			pre.Next = first
			pre = first
			first = first.Next
		}
		if last != nil {
			pre.Next = last
			pre = last
			last = last.Next
		}
	}
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	if head.Next == nil {
		return head
	}
	first, second := head, head.Next
	for {
		if second.Next == nil {
			second.Next = first
			break
		}
		tmpNode := second.Next
		second.Next = first
		first = second
		second = tmpNode
	}
	head.Next = nil
	return second
}