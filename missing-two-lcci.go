package main

func missingTwo(nums []int) []int {
	cache := make(map[int]bool)
	for _, num := range nums {
		cache[num] = true
	}
	var res []int
	for i := 1; i <= len(nums)+2; i++ {
		if !cache[i] {
			res = append(res, i)
		}
	}
	return res
}
