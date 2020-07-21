package main

func maxProfit(prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}
	dq := make([][]int, n)
	for i := 0; i < n; i++ {
		dq[i] = make([]int, 2)
	}
	// dq[i][j]，i标识第几天， j标识持有股票状态， 1标识持有股票， 0标识未持有股票
	for i := 0; i < n; i++ {
		if i == 0 {
			dq[i][0] = 0
			dq[i][1] = -prices[0]
			continue
		}
		dq[i][0] = max(dq[i-1][0], dq[i-1][1]+prices[i])
		dq[i][1] = max(dq[i-1][1], -prices[i])
	}
	// 0肯定比1利润大
	return dq[n-1][0]
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}
