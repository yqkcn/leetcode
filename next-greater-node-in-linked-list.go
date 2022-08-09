package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func nextLargerNodes(head *ListNode) []int {
	nums := make(map[int]int)
	var res []int
	for i := 0; head != nil; i++ {
		nums[i] = head.Val
		// 往前找直到找到大于当前值的
		for j := i - 1; j >= 0 && nums[j] < head.Val; j-- {
			// 还没有最大值，判断当前值是否满足
			if res[j] == 0 {
				res[j] = head.Val
			}
		}
		// 当前节点加 0
		res = append(res, 0)
		head = head.Next
	}
	return res
}
