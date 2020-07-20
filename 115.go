package main

import (
	"strings"
)

func numDistinct(s string, t string) int {
	m, n := len(s), len(t)
	if m == 0 || n == 0 {
		return 0
	}
	dq := make([][]int, m)
	for i := 0; i < m; i++ {
		dq[i] = make([]int, n)
		dq[i][0] = strings.Count(s[:i+1], string(t[0]))
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			// 字符串长度不够
			if i == 0 || j == 0 || i < j {
				continue
			}
			// 结尾字母相同
			if s[i] == t[j] {
				dq[i][j] = dq[i-1][j-1] + dq[i-1][j]
			} else {
				dq[i][j] = dq[i-1][j]
			}

		}
	}
	// fmt.Printf("%v", dq)
	return dq[m-1][n-1]
}

func main() {
	numDistinct("rabbbit", "rabbit")
}
