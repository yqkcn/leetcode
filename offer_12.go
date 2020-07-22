package main

func exist(board [][]byte, word string) bool {
	if board == nil || len(board) == 0 || len(board[0]) == 0 {
		return false
	}
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if findPath(board, word, i, j, 0) {
				return true
			}
		}
	}
	return false
}

func findPath(board [][]byte, word string, i int, j int, k int) bool {
	// 匹配到
	if k == len(word) {
		return true
	}
	// 判断是否越界
	if i < 0 || i >= len(board) || j < 0 || j >= len(board[0]) {
		return false
	}

	// 当前字符匹配不到
	if board[i][j] != word[k] {
		return false
	}

	// 当前字符匹配到，尝试匹配上下左右
	// 将当前字符换为空格， 防止重复经过
	tmp := board[i][j]
	board[i][j] = ' '
	// 上
	if findPath(board, word, i-1, j, k+1) {
		return true
	}
	// 下
	if findPath(board, word, i+1, j, k+1) {
		return true
	}
	// 左
	if findPath(board, word, i, j-1, k+1) {
		return true
	}
	// 右
	if findPath(board, word, i, j+1, k+1) {
		return true
	}
	// 替换为原有字符
	board[i][j] = tmp
	return false
}
