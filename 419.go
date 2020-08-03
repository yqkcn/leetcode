package main

func countBattleships(board [][]byte) int {
	res := 0
	if len(board) == 0 || len(board[0]) == 0 {
		return res
	}
	m, n := len(board), len(board[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == 'X' {
				// 判断左侧和上方是否也是 X
				if i-1 >= 0 && board[i-1][j] == 'X' {
					continue
				}
				if j-1 >= 0 && board[i][j-1] == 'X' {
					continue
				}
				res++
			}
		}
	}
	return res
}
