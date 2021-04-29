package main

func missingNumber(nums []int) int {
	cache := make(map[int]bool)
	for _, num := range nums {
		cache[num] = true
	}
	res := 0
	for i := 0; i <= len(nums); i++ {
		if _, ok := cache[i]; !ok {
			res = i
			break
		}
	}
	return res
}
