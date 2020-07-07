package main

func missingNumber(nums []int) int {
	n := len(nums)
	return n * (n + 1) / 2 - sum(nums)
}

func sum(nums []int) int {
	res := 0
	for _, num := range nums {
		res += num
	}
	return res
}
