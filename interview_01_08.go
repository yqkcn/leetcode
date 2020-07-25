package main

func setZeroes(matrix [][]int) {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return
	}
	zerRow := make(map[int]bool)
	zerCol := make(map[int]bool)
	m, n := len(matrix), len(matrix[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				zerRow[i] = true
				zerCol[j] = true
			}
		}
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if zerRow[i] || zerCol[j] {
				matrix[i][j] = 0
			}
		}
	}
}
