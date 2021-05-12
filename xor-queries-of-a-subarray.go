package main

func xorQueries(arr []int, queries [][]int) []int {
	if arr == nil {
		return []int{}
	}
	xorArr := []int{arr[0]}
	for i := 1; i < len(arr); i++ {
		xorArr = append(xorArr, arr[i]^xorArr[len(xorArr)-1])
	}
	var res []int
	for _, query := range queries {
		if query[0] == 0 {
			res = append(res, xorArr[query[1]])
		} else {
			res = append(res, xorArr[query[0]-1]^xorArr[query[1]])
		}
	}
	return res
}
