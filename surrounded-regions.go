package main

func solve(board [][]byte) {
	if board == nil {
		return
	}
	var queue [][2]int
	// 遍历四条边找到边上为O的位置
	m, n := len(board), len(board[0])
	// 上下
	for j := 0; j < n; j++ {
		if board[0][j] == 'O' {
			queue = append(queue, [2]int{0, j})
		}
		if board[m-1][j] == 'O' {
			queue = append(queue, [2]int{m - 1, j})
		}
	}
	// 左右
	for i := 0; i < m; i++ {
		if board[i][0] == 'O' {
			queue = append(queue, [2]int{i, 0})
		}
		if board[i][n-1] == 'O' {
			queue = append(queue, [2]int{i, n - 1})
		}
	}
	cached := make(map[[2]int]bool)
	// 找到每个O点的邻居，如果也是O加入队列
	for len(queue) > 0 {
		for _, q := range queue {
			cached[q] = true
		}
		var newQueue [][2]int
		for _, q := range queue {
			// 添加邻居
			i, j := q[0], q[1]
			for _, p := range [][2]int{{i, j - 1}, {i, j + 1}, {i - 1, j}, {i + 1, j}} {
				if _, ok := cached[p]; ok {
					continue
				}
				k, l := p[0], p[1]
				if 0 <= k && k < m && 0 <= l && l < n && board[k][l] == 'O' {
					newQueue = append(newQueue, [2]int{k, l})
				}
			}
		}
		queue = newQueue
	}
	// 遍历替换
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == 'X' {
				continue
			}
			if _, ok := cached[[2]int{i, j}]; !ok {
				board[i][j] = 'X'
			}
		}
	}
}
