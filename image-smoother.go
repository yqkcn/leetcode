package main

func imageSmoother(M [][]int) [][]int {
	if M == nil {
		return M
	}
	r, c := len(M), len(M[0])
	var grid [][]int
	for i := 0; i < r; i++ {
		grid = append(grid, make([]int, c))
	}
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			points := [][2]int{
				{i, j},
				{i, j - 1},
				{i, j + 1},
				{i + 1, j},
				{i + 1, j - 1},
				{i + 1, j + 1},
				{i - 1, j},
				{i - 1, j - 1},
				{i - 1, j + 1},
			}
			sum := 0
			num := 0
			for _, p := range points {
				if p[0] < 0 || p[0] >= r || p[1] < 0 || p[1] >= c {
					continue
				}
				sum += M[p[0]][p[1]]
				num++
			}
			grid[i][j] = sum / num
		}
	}
	return grid
}
