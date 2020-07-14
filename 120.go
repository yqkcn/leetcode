package main

func minimumTotal(triangle [][]int) int {
	if triangle == nil {
		return 0
	}
	if len(triangle) == 1 {
		return triangle[0][0]
	}
	res := []int{triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]}
	for _, row := range triangle[2:] {
		var cur []int
		for i, num := range row {
			if i == 0 {
				cur = append(cur, res[0]+num)
				continue
			}
			if i == len(row)-1 {
				cur = append(cur, res[len(res)-1]+num)
				continue
			}
			if res[i] < res[i-1] {
				cur = append(cur, res[i]+num)
			} else {
				cur = append(cur, res[i-1]+num)
			}
		}
		res = cur
	}
	path := 10000000000000
	for _, num := range res {
		if num < path {
			path = num
		}
	}
	return path
}
