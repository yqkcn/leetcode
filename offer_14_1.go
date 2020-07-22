package main

func cuttingRope(n int) int {
	dq := make([]int, n+1)
	dq[0] = 0
	dq[1] = 1
	for i := 2; i <= n; i++ {
		for j := 1; j < i; j++ {
			dq[i] = max(dq[i], max(dq[j], j)*max(dq[i-j], i-j))
		}
	}
	return dq[n]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
