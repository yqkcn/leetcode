package main

func minStartValue(nums []int) int {
	res := 101
	sum := 0
	for _, num := range nums {
		sum += num
		if sum < res {
			res = sum
		}
	}
	if res >= 0 {
		return 1
	}
	return res*-1 + 1
}
