package main

import "strings"

func minFlips(target string) int {
	if len(target) == 0 {
		return 0
	}
	target = strings.TrimLeft(target, "0")
	if len(target) == 0 {
		return 0
	}
	// 从第一个1开始，计算1和0的段数
	res := 1
	for i := 0; i < len(target)-1; i++ {
		if target[i] != target[i+1] {
			res++
		}
	}
	return res
}
