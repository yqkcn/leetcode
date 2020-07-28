package main

func longestIncreasingPath(matrix [][]int) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	res := 0
	m, n := len(matrix), len(matrix[0])
	cache := make(map[[2]int]bool)
	resCache := make(map[[2]int]int)
	var dfs func(int, int, int) int
	dfs = func(i int, j int, k int) int {
		if num, ok := resCache[[2]int{i, j}]; ok {
			return num + k - 1
		}
		curRes := k
		cache[[2]int{i, j}] = true
		// 上下左右
		if i-1 >= 0 && matrix[i-1][j] > matrix[i][j] && !cache[[2]int{i - 1, j}] {
			curRes = max(dfs(i-1, j, k+1), curRes)
		}
		if i+1 < m && matrix[i+1][j] > matrix[i][j] && !cache[[2]int{i + 1, j}] {
			curRes = max(dfs(i+1, j, k+1), curRes)
		}
		if j-1 >= 0 && matrix[i][j-1] > matrix[i][j] && !cache[[2]int{i, j - 1}] {
			curRes = max(dfs(i, j-1, k+1), curRes)
		}
		if j+1 < n && matrix[i][j+1] > matrix[i][j] && !cache[[2]int{i, j + 1}] {
			curRes = max(dfs(i, j+1, k+1), curRes)
		}
		cache[[2]int{i, j}] = false
		return curRes
	}
	// 每个点作为起点试一波
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			num := dfs(i, j, 1)
			res = max(num, res)
			resCache[[2]int{i, j}] = num
		}
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
