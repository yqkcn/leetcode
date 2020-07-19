package main

import "sort"

type sCount struct {
	str string
	count int
}

func frequencySort(s string) string {
	if len(s) < 2 {
		return s
	}
	count := make(map[string]int)
	for _, str := range s {
		count[string(str)]++
	}
	var sCounts []sCount
	for k, v := range count {
		sCounts = append(sCounts, sCount{str: k, count: v})
	}
	sort.SliceStable(sCounts, func(i, j int) bool {
		return sCounts[i].count > sCounts[j].count
	})
	var res string
	for _, str := range sCounts {
		for i:=0;i<str.count;i++{
			res += str.str
		}
	}
	return res
}
