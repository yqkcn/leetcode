package main

import "sort"

func reconstructQueue(people [][]int) [][]int {
	var highs []int
	cache := make(map[int]bool)
	highSorts := make(map[int][][]int)
	for _, human := range people {
		if _, ok := cache[human[0]]; !ok {
			cache[human[0]] = true
			highs = append(highs, human[0])
		}
		highSorts[human[0]] = append(highSorts[human[0]], human)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(highs)))
	var res [][]int
	for _, high := range highs {
		highSort := highSorts[high]
		sort.SliceStable(highSort, func(i, j int) bool {
			return highSort[i][1] < highSort[j][1]
		})
		for _, human := range highSort {
			res = append(res, []int{})
			copy(res[human[1]+1:], res[human[1]:])
			res[human[1]] = human
		}
	}
	return res
}
