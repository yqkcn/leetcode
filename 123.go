package main

import "math"

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}

	max := func(x, y int) int {
		if x < y {
			return y
		}
		return x
	}
	tmp1_0, tmp1_1, tmp2_0, tmp2_1 := 0, math.MinInt32, 0, math.MinInt32
	for i := 0; i < len(prices); i++ {
		tmp1_1 = max(tmp1_1, -prices[i])
		tmp1_0 = max(tmp1_0, tmp1_1+prices[i])
		tmp2_0 = max(tmp2_0, tmp2_1+prices[i])
		tmp2_1 = max(tmp2_1, tmp1_0-prices[i])
	}
	return tmp2_0

}
