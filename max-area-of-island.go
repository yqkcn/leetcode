package main

func maxAreaOfIsland(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	var dfs2 func(r, c int) int
	dfs2 = func(r, c int) int {
		if grid[r][c] != 1 {
			return 0
		} else {
			// 找到所有的邻居
			idxes := [][2]int{{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}}
			num := 1
			grid[r][c] = 2
			for _, point := range idxes {
				l, k := point[0], point[1]
				if l < 0 || l >= m || k < 0 || k >= n {
					continue
				} else {
					num += dfs2(l, k)
				}
			}
			return num
		}
	}
	answer := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				answer = Max2(answer, dfs2(i, j))
			}
		}
	}
	return answer
}

func Max2(x, y int) int {
	if x >= y {
		return x
	} else {
		return y
	}
}
