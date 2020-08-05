package main

import (
	"sort"
	"strconv"
)

func findRelativeRanks(nums []int) []string {
	var newNums []int
	newNums = append(newNums, nums...)
	sort.Slice(newNums, func(i, j int) bool {
		return newNums[i] > newNums[j]
	})
	cache := make(map[int]string)
	for i, num := range newNums {
		var cur string
		if i == 0 {
			cur = "Gold Medal"
		} else if i == 1 {
			cur = "Silver Medal"
		} else if i == 2 {
			cur = "Bronze Medal"
		} else {
			cur = strconv.Itoa(i + 1)
		}
		cache[num] = cur
	}
	var res []string
	for _, num := range nums {
		res = append(res, cache[num])
	}
	return res
}
