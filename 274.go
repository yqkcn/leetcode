package main

func hIndex(citations []int) int {
	if citations == nil {
		return 0
	}
	res := 0
	for i := 1; i < len(citations)+1; i++ {
		if getNumIndex(citations, i) {
			res = i
		}
	}
	return res
}

func getNumIndex(nums []int, target int) bool {
	res := 0
	for _, num := range nums {
		if num >= target {
			res += 1
		}
	}
	if res >= target {
		return true
	}
	return false
}
