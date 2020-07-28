package main

import (
	"sort"
	"strings"
)

func maxProduct(words []string) int {
	if len(words) < 2 {
		return 0
	}
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) > len(words[j])
	})
	res := 0
	for i := 0; i < len(words)-1; i++ {
		// 最大也没超过当前最大，不继续遍历
		if len(words[i])*len(words[i]) <= res {
			continue
		}
		for j := i + 1; j < len(words); j++ {
			if !haxStr(words[i], words[j]) {
				res = max(res, len(words[i])*len(words[j]))
			}
		}
	}
	return res
}

func haxStr(s1, s2 string) bool {
	// 判断两个字符串是否有公共字母
	for _, str := range s1 {
		if strings.Contains(s2, string(str)) {
			return true
		}
	}
	return false
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
