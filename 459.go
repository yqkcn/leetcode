package main

import "strings"

func repeatedSubstringPattern(s string) bool {
	if len(s) < 2 {
		return false
	}
	res := false
	for i:=1;i<len(s);i++{
		curStr := s[:i]
		// 判断长度是否满足
		if len(s)%len(curStr) != 0 {
			continue
		}
		curRes := true
		for j:=i;j<len(s);j+=i{
			if !strings.HasPrefix(s[j:], curStr) {
				curRes = false
				break
			}
		}
		if curRes {
			res = curRes
			break
		}
	}
	return res
}
