package main

import (
	"sort"
)

func twoSum(n int) []float64 {
	p := 1.0 / 6
	cache := map[int]float64{1: p, 2: p, 3: p, 4: p, 5: p, 6: p}
	for i := 2; i <= n; i++ {
		newCache := make(map[int]float64)
		for j := 1; j <= 6; j++ {
			for k, v := range cache {
				newCache[k+j] += v * p
			}
		}
		cache = newCache
	}
	var keys []int
	for k, _ := range cache {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	var res []float64
	for _, k := range keys {
		res = append(res, cache[k])
	}
	return res
}

func main() {
	twoSum(2)
}
