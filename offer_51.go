package main

func reversePairs(nums []int) int {
	if len(nums) < 2 {
		return 0
	}
	res := 0
	minNum := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] < minNum {
			res += i
			minNum = nums[i]
		} else {
			for j := 0; j < i; j++ {
				if nums[j] > nums[i] {
					res += 1
				}
			}
		}
	}
	return res
}
