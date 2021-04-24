package main

func matrixReshape(nums [][]int, r int, c int) [][]int {
	if nums == nil {
		return nums
	}
	m, n := len(nums), len(nums[0])
	if m*n != r*c {
		return nums
	}
	var items []int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			items = append(items, nums[i][j])
		}
	}
	var res [][]int
	for i := 0; i < r; i++ {
		res = append(res, make([]int, c))
	}
	idx := 0
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			res[i][j] = items[idx]
			idx++
		}
	}
	return res
}
