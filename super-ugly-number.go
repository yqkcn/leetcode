package main

import "math"

func nthSuperUglyNumber(n int, primes []int) int {
	cache := make(map[int]int)
	for _, p := range primes {
		cache[p] = 1
	}
	dp := make([]int, n+1)
	dp[1] = 1
	for i := 2; i <= n; i++ {
		minNum := math.MaxInt32
		for k, v := range cache {
			if dp[v]*k < minNum {
				minNum = dp[v] * k
			}
		}
		for k, v := range cache {
			if dp[v]*k == minNum {
				cache[k]++
			}
		}
		dp[i] = minNum
	}
	return dp[n]
}
