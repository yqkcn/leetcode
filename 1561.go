package main

import "sort"

func maxCoins(piles []int) int {
	sort.Ints(piles)
	sum := 0
	for i := len(piles)/3; i < len(piles); i += 2 {
		sum += piles[i]
	}
	return sum
}
