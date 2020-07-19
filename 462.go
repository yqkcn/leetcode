package main

import "sort"

func minMoves2(nums []int) int {
	sort.Ints(nums)
	rlt := 0
	pos := 0
	if len(nums)%2 == 0 {
		pos = len(nums)/2
	} else {
		pos = (len(nums)+1)/2
	}


	for _,num := range nums[:pos] {
		rlt += nums[pos-1]- num
	}
	for _, num := range nums[pos:] {
		rlt += num - nums[pos-1]
	}
	return rlt
}
