package main

func maxProfit(k int, prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}
	if k > n/2 {
		k = n / 2
	}
	dq := make([][][]int, n)
	for i := 0; i < n; i++ {
		dq[i] = make([][]int, k+1)
		for j := 0; j < k+1; j++ {
			dq[i][j] = make([]int, 2)
		}
	}
	// dq[i][k][j]，i标识第几天，k标识交易次数， j标识持有股票状态， 1标识持有股票， 0标识未持有股票
	for i := 0; i < n; i++ {
		for j := 1; j < k+1; j++ {
			// i 为 0
			if i == 0 {
				dq[i][j][0] = 0
				dq[i][j][1] = -prices[0]
				continue
			}
			dq[i][j][0] = max(dq[i-1][j][0], dq[i-1][j][1]+prices[i])
			dq[i][j][1] = max(dq[i-1][j][1], dq[i-1][j-1][0]-prices[i])

		}
	}
	// 0肯定比1利润大
	return dq[n-1][k][0]
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}
