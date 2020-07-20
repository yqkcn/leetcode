package main

import "fmt"

func isInterleave(s1 string, s2 string, s3 string) bool {
	return inner(s1, s2, s3, make(map[[3]string]bool))
}

func inner(s1 string, s2 string, s3 string, cache map[[3]string]bool) bool {
	//fmt.Printf("%s:%s:%s\n", s1, s2, s3)
	key := [3]string{s1, s2, s3}
	if res, ok := cache[key]; ok {
		return res
	}
	// 其中一个字符串已经空， 判断相等
	if len(s1) == 0 || len(s2) == 0 {
		cache[key] = s3 == s1+s2
		return cache[key]
	}
	// 直接相等
	if s3 == s1+s2 || s3 == s2+s1 {
		cache[key] = true
		return true
	}
	// 首字母不同， 不是扰乱字符串
	if s3[0] != s1[0] && s3[0] != s2[0] {
		cache[key] = false
		return false
	}
	// s1 和 s2 的首字母都可取
	if s1[0] == s3[0] && s2[0] == s3[0] {
		cache[key] = isInterleave(s1[1:], s2, s3[1:]) || isInterleave(s1, s2[1:], s3[1:])
		return cache[key]
	}
	// s1
	if s1[0] == s3[0] {
		cache[key] = isInterleave(s1[1:], s2, s3[1:])
		return cache[key]
	}
	cache[key] = isInterleave(s1, s2[1:], s3[1:])
	return cache[key]
}

func main() {
	fmt.Print(isInterleave("aabcc", "dbbca", "aadbbbaccc"))
}
