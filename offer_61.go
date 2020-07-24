package main

import "sort"

func isStraight(nums []int) bool {
	sort.Ints(nums)
	zeroNum := 0
	reduce := 0
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == 0 {
			zeroNum++
		} else {
			if nums[i] == nums[i+1] {
				return false
			}
			reduce += nums[i+1] - nums[i] - 1
		}
	}
	return zeroNum >= reduce
}
