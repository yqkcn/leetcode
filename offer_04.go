package main

func findNumberIn2DArray(matrix [][]int, target int) bool {
	if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}
	n, m := len(matrix), len(matrix[0])
	for i := 0; i < n; i++ {
		if target > matrix[i][m-1] {
			continue
		}
		if target < matrix[i][0] {
			return false
		}
		for j := 0; j < m; j++ {
			if matrix[i][j] == target {
				return true
			}
		}
	}
	return false
}
