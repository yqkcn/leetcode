package main

import "sort"

func wiggleSort(nums []int) {
	sort.Ints(nums)
	res := []int{}
	left, right := 0, len(nums)-1
	for left < right {
		res = append(res, nums[left])
		res = append(res, nums[right])
		left++
		right--
	}
	if left == right {
		res = append(res, nums[left])
	}
	copy(nums, res)
}
