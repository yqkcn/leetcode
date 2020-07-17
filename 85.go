package main

func maximalRectangle(matrix [][]byte) int {
	area := 0
	// 空
	if matrix == nil || len(matrix) == 0 {
		return area
	}
	m, n := len(matrix), len(matrix[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			// 0直接跳过
			if matrix[i][j] == '0' {
				continue
			}
			// 只取右下角的数据，左上方不用考虑，因为之前的数已经搜索过了
			maxL := n
			for k := i; k < m; k++ {
				for l := j; l < maxL; l++ {
					// 一个子矩阵全是1，比较子矩阵面积和最大面积
					if isAllOne(matrix, i, j, k, l) {
						curArea := (k - i + 1) * (l - j + 1)
						if curArea > area {
							area = curArea
						}
					} else {
						maxL = l
						break
					}
				}
			}
		}
	}
	return area
}

func isAllOne(matrix [][]byte, i int, j int, k int, l int) bool {
	// 判断所给二维矩阵是否全是 1
	// m,n 是起始下标
	for m := i; m <= k; m++ {
		for n := j; n <= l; n++ {
			if matrix[m][n] != '1' {
				return false
			}
		}
	}
	return true
}

func main() {

}
