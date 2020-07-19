package main

import "sort"

func minMoves(nums []int) int {
	if len(nums)<=1{
		return 0
	}
	sort.Ints(nums)
	count:=0
	for i:=1;i<len(nums);i++{
		count+=nums[i]-nums[0]
	}
	return count
}