package main

func repeatedNTimes(nums []int) int {
	visited := make(map[int]bool)
	res := 0
	for _, num := range nums {
		if visited[num] {
			res = num
			break
		} else {
			visited[num] = true
		}
	}
	return res
}
