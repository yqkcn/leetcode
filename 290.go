package main

import "strings"

func wordPattern(pattern string, str string) bool {
	sign := make(map[string]string)
	set := make(map[string]bool)
	strs := strings.Split(str, " ")
	if len(strs) != len(pattern) {
		return false
	}
	pat := []byte(pattern)
	for i:=0;i<len(strs);i++{
		if p, ok := sign[string(pat[i])]; ok{
			if p != strs[i] {
				return false
			}
			continue
		}
		if _, ok := set[strs[i]]; ok {
			return false
		}
		sign[string(pat[i])] = strs[i]
		set[strs[i]] = true
	}
	return true
}
