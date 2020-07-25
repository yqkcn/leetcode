package main

func findPeakElement(nums []int) int {
	if len(nums) == 1 {
		return 0
	}
	for i, num := range nums {
		if i == 0 {
			if num > nums[i+1] {
				return i
			}
		} else if i == len(nums) - 1 {
			if num > nums[i-1] {
				return i
			}
		} else {
			if num > nums[i-1] && num > nums[i+1] {
				return i
			}
		}
	}
	return 0
}
