package main

import "fmt"

func main() {
	fmt.Print(isIsomorphic("ab", "aa"))
}

func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	cache := make(map[string]string)
	set := make(map[string]bool)
	for i := 0; i < len(t); i++ {
		if _, ok := cache[string(t[i])]; !ok {
			if set[string(s[i])] {
				return false
			}
			cache[string(t[i])] = string(s[i])
			set[string(s[i])] = true
		} else {
			if cache[string(t[i])] != string(s[i]) {
				return false
			}
		}
	}
	return true
}
