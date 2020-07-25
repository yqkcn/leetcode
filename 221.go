package main

func maximalSquare(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	m, n := len(matrix), len(matrix[0])
	area := 0
	for i:=0;i<m;i++{
		for j:=0;j<n;j++{
			if matrix[i][j] == '0' {
				continue
			}
			area = max(area, 1)
			// 较短的边决定正方形
			for k:=1;k<=min(m-i, n-j);k++{
				// 全为一
				all := true
				for r:=i;r<=i+k;r++{
					if !all {
						break
					}
					for c:=j;c<=j+k;c++{
						if matrix[r][c] == '0' {
							all = false
							break
						}
					}
				}
				if !all {
					break
				}
				area = max(area, k*k)
			}
		}
	}
	return area
}

func max(a,b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a,b int) int {
	if a<b{
		return a
	}
	return b
}

func main() {

}
