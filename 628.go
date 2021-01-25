package main

import "sort"

func maximumProduct(nums []int) int {
	sort.Ints(nums)
	l := len(nums)
	a := max(nums[0]*nums[1]*nums[2], nums[0]*nums[1]*nums[l-1])
	a = max(a, nums[0]*nums[l-2]*nums[l-1])
	a = max(a, nums[l-3]*nums[l-2]*nums[l-1])
	return a
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
