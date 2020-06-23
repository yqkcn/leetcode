package main

import "fmt"

func main() {
	params := [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}
	fmt.Print(spiralOrder(params))
	params = [][]int{{2, 5}, {8, 4}, {0, -1}}
	fmt.Print(spiralOrder(params))
}

func spiralOrder(matrix [][]int) []int {
	var res []int
	if len(matrix) == 0 {
		return res
	}
	min_m, max_m := 0, len(matrix)-1
	min_n, max_n := 0, len(matrix[0])-1
	m, n := 0, 0
	target := len(matrix) * len(matrix[0])
	for len(res) != target {
		if m == min_m {
			if n == min_n {
				for i := n; i <= max_n; i++ {
					res = append(res, matrix[m][i])
				}
				m += 1
				n = max_n
				min_m += 1
			} else {
				for i := m; i <= max_m; i++ {
					res = append(res, matrix[i][n])
				}
				max_n -= 1
				n -= 1
				m = max_m
			}
			continue
		} else {
			if n == min_n {
				for i := m; i >= min_m; i-- {
					res = append(res, matrix[i][n])
				}
				n += 1
				min_n += 1
				m = min_m
			} else {
				for i := n; i >= min_n; i-- {
					res = append(res, matrix[m][i])
				}
				max_m -= 1
				m -= 1
				n = min_n
			}
		}
	}
	return res
}
