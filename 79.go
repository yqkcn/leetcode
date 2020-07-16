package main

func searchMatrix(matrix [][]int, target int) bool {
	if matrix == nil || len(matrix) == 0 {
		return false
	}
	m, n := len(matrix), len(matrix[0])
	left, right := 0, m*n-1
	var res bool
	for left <= right {
		if left+1 == right || left == right {
			res = matrix[left/n][left%n] == target || matrix[right/n][right%n] == target
			break
		}

		mid := (left + right) / 2
		midNum := matrix[mid/n][mid%n]
		if midNum == target {
			res = true
			break
		}
		if midNum > target {
			right = mid
			continue
		}
		if midNum < target {
			left = mid
			continue
		}
	}
	return res
}
