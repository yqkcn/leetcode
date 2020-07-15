package main

import "fmt"

func numTrees(n int) int {
	dq := []int{1, 1, 2}
	if n < 3 {
		return dq[n]
	}
	for i := 3; i <= n; i++ {
		num := 0
		for j := 1; j <= i; j++ {
			// 分成左右两个部分，两部分可能情况相乘
			num += dq[j-1] * dq[i-j]
		}
		dq = append(dq, num)
	}
	return dq[len(dq)-1]
}

func main() {
	fmt.Print(numTrees(3))
}
