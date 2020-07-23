package main

func maxValue(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	m, n := len(grid), len(grid[0])
	dq := make([][]int, m)
	for i := 0; i < m; i++ {
		dq[i] = make([]int, n)
	}
	dq[0][0] = grid[0][0]
	for i := 1; i < n; i++ {
		dq[0][i] = dq[0][i-1] + grid[0][i]
	}
	for i := 1; i < m; i++ {
		dq[i][0] = dq[i-1][0] + grid[i][0]
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			dq[i][j] = grid[i][j] + max(dq[i][j-1], dq[i-1][j])
		}
	}
	return dq[m-1][n-1]
}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	maxValue([][]int{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}})
}
