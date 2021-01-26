package main

import "sort"

func numEquivDominoPairs(dominoes [][]int) int {
	counter := make(map[[2]int]int)
	// 遍历一遍计数
	for _, d := range dominoes {
		// 排序保持一直
		sort.Ints(d)
		cur := [2]int{d[0], d[1]}
		_, ok := counter[cur]
		if ok {
			counter[cur]++
		} else {
			counter[cur] = 1
		}
	}
	// 遍历所有的计数，每个类型出现次数为 n * (n - 1) / 2
	res := 0
	for _, v := range counter {
		res += v * (v - 1) / 2
	}
	return res
}

func main() {
	numEquivDominoPairs([][]int{{1,2},{2,1},{3,4},{5,6}})
}