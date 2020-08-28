package main

import (
	"fmt"
	"sort"
)

func mostVisited(n int, rounds []int) []int {
	cache := make(map[int]int)
	cache[rounds[0]]++
	for i := 1; i < len(rounds); i++ {
		fmt.Print(cache)
		if rounds[i] > rounds[i-1] {
			for j := rounds[i-1] + 1; j <= rounds[i]; j++ {
				cache[j]++
			}
		} else if rounds[i] <= rounds[i-1] {
			for j := rounds[i-1]+1; j <= n; j++ {
				cache[j]++
			}
			for j := 1; j <= rounds[i]; j++ {
				cache[j]++
			}
		}
	}
	maxNum := 0
	for _, v := range cache {
		if v > maxNum {
			maxNum = v
		}
	}
	var res []int
	for k, v := range cache {
		if v == maxNum {
			res = append(res, k)
		}
	}
	sort.Ints(res)
	return res
}

func main() {
	mostVisited(4, []int{1,3,1,2})
}