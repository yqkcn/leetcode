package main

func islandPerimeter(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	res := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				res += countL(grid, i, j)
			}
		}
	}
	return res
}

func countL(grid [][]int, i int, j int) int {
	// 判断上下左右邻居，有一个周长减去一
	res := 4
	if i-1 >= 0 && grid[i-1][j] == 1 {
		res--
	}
	if i+1 < len(grid) && grid[i+1][j] == 1 {
		res--
	}
	if j-1 >= 0 && grid[i][j-1] == 1 {
		res--
	}
	if j+1 < len(grid[0]) && grid[i][j+1] == 1 {
		res--
	}
	return res
}
