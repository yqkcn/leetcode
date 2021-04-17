package main

func arraySign(nums []int) int {
	gt := 0
	for _, num := range nums {
		if num == 0 {
			return 0
		}
		if num < 0 {
			gt++
		}
	}
	if gt % 2 == 0 {
		return 1
	}
	return -1
}
