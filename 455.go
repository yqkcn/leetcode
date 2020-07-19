package main

import "sort"

func findContentChildren(g []int, s []int) int {
	sort.Ints(g)
	sort.Ints(s)
	res := 0
	sIdx := 0
	for i:=0;i<len(g);i++{
		if sIdx == len(s){
			break
		}
		for j:=sIdx;j<len(s);j++{
			if s[sIdx] >= g[i] {
				res++
				sIdx++
				break
			}
			sIdx ++
		}
	}
	return res
}
