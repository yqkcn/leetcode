package main

func searchMatrix(matrix [][]int, target int) bool {
	if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}
	n, m := len(matrix), len(matrix[0])
	row, col := n-1, 0
	for row >= 0 && col < m {
		if matrix[row][col] > target {
			row--
		} else {
			if matrix[row][col] < target {
				col++
			} else {
				return true
			}
		}
	}
	return false
}
