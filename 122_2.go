package main

import "math"

func maxProfit(prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}
	dq_0, dq_1 := 0, math.MinInt64
	for i := 0; i < n; i++ {
		tmp := dq_0
		dq_0 = max(dq_0, dq_1+prices[i])
		dq_1 = max(dq_1, tmp-prices[i])
	}
	// 0肯定比1利润大
	return dq_0
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}
