package main

func buildArray(target []int, n int) []string {
	visited := make(map[int]bool)
	maxNum := 0
	for _, num := range target {
		if num > maxNum {
			maxNum = num
		}
		visited[num] = true
	}
	var res []string
	for i := 1; i <= maxNum; i++ {
		if visited[i] {
			res = append(res, "Push")
		} else {
			res = append(res, "Push")
			res = append(res, "Pop")
		}
	}
	return res
}
