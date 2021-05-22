package main

func swimInWater(grid [][]int) int {
	if grid == nil {
		return 0
	}
	m, n := len(grid), len(grid[0])
	// 开始时间为起点终点较大值
	startTime := grid[0][0]
	if grid[m-1][n-1] > startTime {
		startTime = grid[m-1][n-1]
	}
	// 搜索成功标志
	success := false
	// 记录已经标记的
	visited := make(map[[2]int]bool)
	// 深度搜索，起点能到达的点标记为 -1， 终点能到达的点标记为 -2
	var dfs func(int, int, int)
	// i, j 为坐标，k 为标记值
	dfs = func(i, j, k int) {
		if i < 0 || i >= m || j < 0 || j >= n {
			return
		}
		// 相遇
		if grid[i][j] < 0 && grid[i][j] != k {
			success = true
			return
		}
		// 已经被淹没标记
		if grid[i][j] <= startTime {
			grid[i][j] = k
			visited[[2]int{i, j}] = true
			// 递归
			for _, p := range [][2]int{{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}} {
				if !visited[p] {
					dfs(p[0], p[1], k)
				}
			}
		}
	}
	for !success {
		visited = make(map[[2]int]bool)
		dfs(0, 0, -1)
		dfs(m-1, n-1, -2)
		if !success{
			startTime++
		}
	}
	return startTime
}
