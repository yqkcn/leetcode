package main

func canPermutePalindrome(s string) bool {
	// 奇数个字母只能有一个
	count := make(map[string]int)
	for _, str := range s {
		count[string(str)]++
	}
	has := false
	for _, v := range count {
		if v%2 != 0 {
			if !has {
				has = true
			} else {
				return false
			}
		}
	}
	return true
}
