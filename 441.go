package main

func arrangeCoins(n int) int {
	if n < 2 {
		return n
	}
	i := 1
	for i*(i+1)/2 <= n {
		i++
	}
	return i - 1
}
