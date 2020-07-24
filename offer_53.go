package main

func missingNumber(nums []int) int {
	for i, num := range nums {
		if i != num {
			return i
		}
	}
	return len(nums)
}
