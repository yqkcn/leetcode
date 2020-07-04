package main

import "fmt"

func main() {
	fmt.Print(partition("aabaa"))
}

func partition(s string) [][]string {
	var cur []string
	return getSubstring(s, cur)
}

func getSubstring(s string, cur []string) [][]string {
	var res [][]string
	if len(s) == 0 {
		res = append(res, cur)
		return res
	}
	for i := 1; i < len(s)+1; i++ {
		if isPalindrome(s[0:i]) {
			var newCur []string
			newCur = append(newCur, cur...)
			newCur = append(newCur, s[0:i])
			res = append(res, getSubstring(s[i:], newCur)...)
		}
	}
	return res
}

func isPalindrome(s string) bool {
	if len(s) == 0 {
		return false
	}
	if len(s) == 1 {
		return true
	}
	i, j := 0, len(s)-1
	for ; i < j; {
		if s[i] == s[j] {
			i += 1
			j -= 1
			continue
		} else {
			return false
		}
	}
	return true
}
